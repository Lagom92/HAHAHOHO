<template>
  <v-responsive min-height="100%">
    <v-btn
    id="searchBtn"
    @click="openSearch"
    v-if="mapWindow === '100%' && searchService"
    fab
    dark
    small
    >
      <v-icon>mdi-magnify</v-icon>
    </v-btn>
    <v-btn
    id="searchBtn"
    @click="closeSearch"
    v-if="mapWindow === '0%' && searchService"
    text
    icon
    >
      <v-icon>mdi-close</v-icon>
    </v-btn>
    <v-responsive id="map" :min-height="mapWindow"></v-responsive>
    <v-container v-if="mapWindow === '0%' && searchService">
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
                <v-list-item
                :key="place.id"
                @click="setPlaces(place.x, place.y)"
                >
                  <v-list-item-content>
                    <v-list-item-title>
                      {{place.place_name}}
                    </v-list-item-title>
                    <v-list-item-subtitle class="mt-2">
                      {{place.road_address_name}}
                    </v-list-item-subtitle>
                    <v-list-item-subtitle>
                      (지번){{place.address_name}}
                    </v-list-item-subtitle>
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
  data () {
    return {
      map: '', // 지도 객체
      mapContainer: '', // 지도를 표시할 div
      mapWindow: '100%', // 지도 창 크기
      ps: '', // 장소 검색 객체 생성
      keyword: '', // 검색 키워드
      places: '', // 검색 결과 15개
      pagination: '', // 검색 결과 이동 기능 객체
      mainMarker: '', // 마커 객체
      infowindow: '', // 마커의 위치 정보를 보여줄 인포윈도우 객체
      geocoder: '', // 주소 좌표 변환 객체
      placeX: '', // 지도의 중심 위도
      placeY: '', // 지도의 중심 경도
      searchRules: [
        v => !!v || '키워드를 입력해주세요!',
        v => v.length <= 15 || '키워드는 15자 이하만 가능합니다!'
      ]
    }
  },
  props: {
    searchService: { type: Boolean, default: false }, // 장소 검색 기능 사용유무
    address: { type: String, default: '광주광역시 광산구 하남산단6번로 133' }, // 입력된 주소
    mapLevel: { type: Number, default: 4 } // 지도의 확대 레벨
  },
  mounted () {
    this.mapContainer = document.getElementById('map')
    this.geocoder = new kakao.maps.services.Geocoder()
    this.infowindow = new kakao.maps.InfoWindow({ zIndex: 1 })
    this.ps = new kakao.maps.services.Places()
    this.mainMarker = new kakao.maps.Marker()
    this.searchLocation(this.address)
    this.createMarker(this.placeY, this.placeX)
  },
  methods: {
    // 지도 생성 함수
    createMap (y, x) {
      let options = {
        center: new kakao.maps.LatLng(y, x),
        level: this.mapLevel,
        mapTypeId: kakao.maps.MapTypeId.ROADMAP
      }
      return new kakao.maps.Map(this.mapContainer, options)
    },

    // 마커 생성 함수
    createMarker (y, x) {
      // 마커가 표시될 위치
      let markerPosition = new kakao.maps.LatLng(y, x)
      this.mainMarker.setPosition(markerPosition)
      // 마커를 지도 위에 표시
      this.mainMarker.setMap(this.map)
      // 마커 드래그 기능 사용 유무
      this.mainMarker.setDraggable(this.searchService)
      // 좌표 값을 주소로 변경
      this.geocoder.coord2Address(
        markerPosition.getLng(),
        markerPosition.getLat(),
        this.setInfo
      )
    },

    // 주소로 좌표를 검색하는 함수
    searchLocation (address) {
      // 주소로 좌표를 검색
      this.geocoder.addressSearch(address, async (result, status) => {
        // 정상적으로 검색이 완료됐다면
        if (status === kakao.maps.services.Status.OK) {
          this.placeY = result[0].y
          this.placeX = result[0].x
          // 지도가 생성되어 있다면 다시 생성하지 않는다
          if (this.map) {
            return false
          }
          // 생성된 지도가 없다면 지도를 만들고 지도위에 마커를 생성
          this.map = await this.createMap(result[0].y, result[0].x)
          await this.createMarker(this.placeY, this.placeX)
        }
      })
    },

    // 상세 주소 검색 콜백 함수
    async setInfo (result, status) {
      // 주소 검색에 성공하면
      if (status === kakao.maps.services.Status.OK) {
        // 도로명 주소가 있다면 도로명 주소, 없다면 번지 주소
        if (result[0].road_address.address_name) {
          await this.$emit('update:address', result[0].road_address.address_name)
        } else {
          await this.$emit('update:address', result[0].address.address_name)
        }
        // 마커 위에 정보 표시
        this.displayInfowindow(this.mainMarker, this.address)
      }
    },

    // 키워드 검색을 요청하는 함수
    searchPlaces () {
      // 장소검색 객체를 통해 키워드로 장소검색을 요청
      this.ps.keywordSearch(this.keyword, this.placesSearchCB)
    },

    // 장소검색이 완료됐을 때 호출되는 콜백함수
    placesSearchCB (data, status, pagination) {
      if (status === kakao.maps.services.Status.OK) {
        // 정상적으로 검색이 완료되면, 실행
        this.places = data
        this.pagination = pagination
      } else if (status === kakao.maps.services.Status.ZERO_RESULT) {
        alert('검색 결과가 존재하지 않습니다.')
        return false
      } else if (status === kakao.maps.services.Status.ERROR) {
        alert('검색 결과 중 오류가 발생했습니다.')
        return false
      }
    },

    // 인포윈도우에 장소명을 표시
    displayInfowindow (marker, title) {
      let content = '<div class="py-1 px-2">' + title + ' .</div>'
      this.infowindow.setContent(content)
      this.infowindow.open(this.map, marker)
    },

    // 검색된 장소 클릭하여 지도에 표시하고 주소를 보냄
    setPlaces (x, y) {
      this.placeX = Number(x)
      this.placeY = Number(y)

      let center = new kakao.maps.LatLng(this.placeY, this.placeX)
      let oneBound = new kakao.maps.LatLngBounds()
      oneBound.extend(center)
      this.map.setBounds(oneBound)
      this.closeSearch()
    },

    // 검색창 여닫기
    closeSearch () {
      this.mapWindow = '100%'
      this.createMarker(this.placeY, this.placeX)
    },
    openSearch () {
      this.mapWindow = '0%'
      this.mainMarker.setMap(null)
      this.infowindow.close()
    }
  }
}
</script>

<style lang="stylus">
#searchBtn
  position absolute
  top 1rem
  right 1rem
  z-index 2
</style>
