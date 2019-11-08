<template>
  <div id="mapWindow" :style="'height: ' + height + '; overflow: auto;'">
    <v-responsive min-height="100%">
      <v-btn
      v-if="mapWindow === '100%' && searchService"
      @click="openSearch"
      id="searchBtn"
      fab
      dark
      small
      >
        <v-icon>mdi-magnify</v-icon>
      </v-btn>
      <v-btn
      v-if="mapWindow === '0%' && searchService"
      @click="closeSearch"
      id="searchBtn"
      text
      icon
      >
        <v-icon>mdi-close</v-icon>
      </v-btn>
      <v-responsive id="map" :min-height="mapWindow"></v-responsive>
      <v-container v-if="mapWindow === '0%' && searchService" id="search">
        <v-row>
          <v-col>
            <v-text-field
            @keydown.enter="searchPlaces"
            v-model="keyword"
            :rules="searchRules"
            :counter="15"
            label="키워드"
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
                <v-row class="justify-center">
                  <div v-for="i in (1, pagination.last)" :key="i">
                    <v-btn
                    @click="pagination.gotoPage(i), scrollToTop()"
                    :color="(i==pagination.current ? 'light-blue' : '')"
                    small
                    text
                    >
                      {{i}}
                    </v-btn>
                  </div>
                </v-row>
              </v-list>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-responsive>
  </div>
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
    address: { type: String, default: '서울' }, // 입력된 주소
    mapLevel: { type: Number, default: 4 }, // 지도의 확대 레벨
    height: { type: String, default: '300px' } // 지도 높이
  },
  mounted () {
    this.mapContainer = document.getElementById('map')
    this.map = this.createMap()
    this.geocoder = new kakao.maps.services.Geocoder()
    this.infowindow = new kakao.maps.InfoWindow({ zIndex: 1 })
    this.ps = new kakao.maps.services.Places()
    this.mainMarker = new kakao.maps.Marker()
    this.searchLocation(this.address)
    if (this.searchService) {
      this.mapEvents()
    }
  },
  methods: {
    // 카카오 맵 이벤트 모음 함수
    mapEvents () {
      // 마커 드래그가 시작하면 infowindow를 닫음
      kakao.maps.event.addListener(this.mainMarker, 'dragstart', () => {
        this.infowindow.close()
      })
      // 마커 드래그가 끝나면 해당위치의 주소를 띄움
      kakao.maps.event.addListener(this.mainMarker, 'dragend', () => {
        // 마커의 좌표값을 저장
        let markerPosition = this.mainMarker.getPosition()
        this.placeX = markerPosition.getLng()
        this.placeY = markerPosition.getLat()
        // 마커 좌표 값을 주소로 변경하고 주소를 마커위에 띄움
        this.geocoder.coord2Address(
          markerPosition.getLng(),
          markerPosition.getLat(),
          this.setInfo
        )
      })
      // 맵을 클릭하면 마커를 이동시킴
      kakao.maps.event.addListener(this.map, 'click', (mouseEvent) => {
        this.infowindow.close()
        // 맵의 중심과 마커의 위치를 클릭한 좌표로 이동
        let latlng = mouseEvent.latLng
        this.mainMarker.setPosition(latlng)
        this.map.panTo(latlng)
        // 좌표값을 저장
        this.placeX = latlng.getLng()
        this.placeY = latlng.getLat()
        // 지도 중심 좌표 값을 주소로 변경하고 주소를 마커위에 띄움
        this.geocoder.coord2Address(
          latlng.getLng(),
          latlng.getLat(),
          this.setInfo
        )
      })
    },

    // 지도 생성 함수
    createMap () {
      let options = {
        center: new kakao.maps.LatLng(33.452613, 126.570888),
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
          // 지도 중심을 주소의 좌표로 이동
          let moveLatLon = new kakao.maps.LatLng(this.placeY, this.placeX)
          this.map.setCenter(moveLatLon)
          // 마커를 주소의 좌표에 생성
          await this.createMarker(this.placeY, this.placeX)
        }
      })
    },

    // 상세 주소 검색 콜백 함수
    async setInfo (result, status) {
      // 주소 검색에 성공하면
      if (status === kakao.maps.services.Status.OK) {
        // 도로명 주소가 있다면 도로명 주소, 없다면 번지 주소
        try {
          await this.$emit('update:address', result[0].road_address.address_name)
        } catch {
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
        console.log(pagination)
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
    },

    // div map의 스크롤을 최상단으로 위치시키는 함수
    scrollToTop () {
      let objMap = document.getElementById('mapWindow')
      objMap.scrollTop = 0
    }
  },
  watch: {
    address: function () {
      if (!this.searchService) {
        this.searchLocation(this.address)
      }
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
