<template>
  <v-responsive min-height="100%">
    <v-btn id="searchBtn" @click="openSearch" v-if="searchWindow === '100%'" color="primary">Open</v-btn>
    <v-btn id="searchBtn" @click="closeSearch" v-else color="primary">Close</v-btn>
    
    <v-responsive id="map" :min-height="searchWindow"></v-responsive>
    
    <v-container v-if="searchWindow === '0%'">
      <v-row>
        <v-col>
          <v-text-field
            v-model="keyword"
            :rules="searchRules"
            :counter="15"
            label="키워드"
            @keydown.enter="searchPlaces"
          ></v-text-field>
          
          <v-card v-if="places">
            <v-list two-line>
              <template v-for="(place, index) in places">
                <v-list-item :key="place.id" @click="setPlaces(place.x, place.y)">
                  <v-list-item-content>
                    <v-list-item-title>{{place.place_name}}</v-list-item-title>
                    <v-list-item-subtitle>{{place.address_name}}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
                <v-divider :key="index"></v-divider>
              </template>
            </v-list>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-responsive>
</template>

<script>
export default {
  name: 'MapService',
  data(){
    return {
      map: '', // 지도 객체
      mapContainer: '', // 지도를 표시할 div
      ps: '', // 장소 검색 객체 생성
      keyword: '', // 검색 키워드
      places: '', // 검색 결과 15개
      pagination: '', // 검색 결과 이동 기능 객체
      searchWindow: '100%', // 장소 검색창 열림유무
      mainMarker: '', // 마커 객체
      infowindow: '', // 마커의 위치 정보를 보여줄 인포윈도우 객체
      markerInfo: '', // 마커 위치 정보
      searchRules: [
        v => !!v || '키워드를 입력해주세요!',
        v => v.length <= 15 || '키워드는 15자 이하만 가능합니다!'
      ],
      placeX: this.mapCenterX,
      placeY: this.mapCenterY
    }
  },
  props: {
    searchService: {type: Boolean, default: false}, // 장소 검색 기능 사용유무
    mapCenterY: {type: Number, default: 35.20553}, // 지도의 중심 경도
    mapCenterX: {type: Number, default: 126.81142}, // 지도의 중심 위도
    mapLevel: {type: Number, default: 4} // 지도의 확대 레벨
  },
  mounted(){
    this.mapContainer = document.getElementById('map')
    this.map = this.createMap(this.placeY, this.placeX)
    this.infowindow = new kakao.maps.InfoWindow({zIndex:1})
    this.ps = new kakao.maps.services.Places()
    this.mainMarker = new kakao.maps.Marker()
    this.createMarker(this.placeX, this.placeY)
  },
  methods: {

    // 지도 생성 함수
    createMap(y, x) {

      let options = {
        center: new kakao.maps.LatLng(y, x),
        level: this.mapLevel,
        mapTypeId : kakao.maps.MapTypeId.ROADMAP
      }

      return new kakao.maps.Map(this.mapContainer, options)
    },

    // 마커 생성 함수
    async createMarker(x, y) {

      // 좌표 값을 주소로 변경해주는 기능을 가진 객체
      let geocoder = new kakao.maps.services.Geocoder()

      // 마커가 표시될 위치
      let markerPosition = new kakao.maps.LatLng(y, x)
      this.mainMarker.setPosition(markerPosition)

      // 마커를 지도 위에 표시
      this.mainMarker.setMap(this.map)

      // 마커 드래그 기능 사용 유무
      this.mainMarker.setDraggable(this.searchService)

      // 좌표 값을 주소로 변경
      geocoder.coord2Address(markerPosition.getLng(), markerPosition.getLat(), this.setInfo)
    },

    // 상세 주소 검색 콜백 함수
    setInfo(result, status) {

      // 주소 검색에 성공하면
      if (status === kakao.maps.services.Status.OK) {

        // 도로명 주소가 있다면 도로명 주소, 없다면 번지 주소
        if (result[0].road_address.address_name) {
          this.markerInfo = result[0].road_address.address_name
        } else {
          this.markerInfo = result[0].address.address_name
        }
        
        // 마커 위에 정보 표시
        this.displayInfowindow(this.mainMarker, this.markerInfo)

      }
    },

    // 키워드 검색을 요청하는 함수
    searchPlaces() {

      // 장소검색 객체를 통해 키워드로 장소검색을 요청
      this.ps.keywordSearch(this.keyword, this.placesSearchCB)
    },

    // 장소검색이 완료됐을 때 호출되는 콜백함수
    placesSearchCB(data, status, pagination) {
      if (status === kakao.maps.services.Status.OK) {

        // 정상적으로 검색이 완료되면, 실행
        this.places = data
        this.pagination = pagination
        
      } else if (status === kakao.maps.services.Status.ZERO_RESULT) {

          alert('검색 결과가 존재하지 않습니다.')
          return

      } else if (status === kakao.maps.services.Status.ERROR) {

        alert('검색 결과 중 오류가 발생했습니다.')
        return
      }
    },

    // 인포윈도우에 장소명을 표시
    displayInfowindow(marker, title) {
      let content = '<div class="py-1 px-2">' + title + ' .</div>'

      this.infowindow.setContent(content)
      this.infowindow.open(this.map, marker)
    },

    // 검색된 장소 클릭하여 지도에 표시
    setPlaces(x, y) {
      this.placeX = Number(x)
      this.placeY = Number(y)

      let center = new kakao.maps.LatLng(this.placeY, this.placeX)
      let oneBound = new kakao.maps.LatLngBounds()
      oneBound.extend(center)

      this.map.setBounds(oneBound)
      this.closeSearch()
    },

    // 검색창 여닫기
    closeSearch() {
      this.searchWindow = '100%'
      this.createMarker(this.placeX, this.placeY)
    },
    openSearch() {
      this.mainMarker.setMap(null)
      this.infowindow.close()
      this.searchWindow = '0%'
    }
  },
}
</script>
<style lang="stylus">
#searchBtn
  position absolute
  top 1rem
  right 1rem
  z-index 10
</style>