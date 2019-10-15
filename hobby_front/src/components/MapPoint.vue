<template>
    <v-container>
        <h1>MapPoint</h1>
        <h3>위도: {{mapCenterY}}</h3>
        <h3>경도: {{mapCenterX}}</h3>
        <div class="map_wrap">
          <div id="map"></div>

          <div id="menu_wrap" class="bg_white">
            <div class="option">
              <div>
                키워드 : <input type="text" id="keyword" size="15" v-model="keyword"/>
                <v-btn @click="searchPlaces()">검색하기</v-btn>
              </div>
            </div>
            <hr>
            <ul id="placesList"></ul>
            <div id="pagination"></div>
          </div>
        </div>
    </v-container>
</template>

<script>
  export default {
    data(){
      return {
        mapContainer: '', // 지도를 표시할 div
        mapCenterY: 33.450701, // 지도의 중심 경도
        mapCenterX: 126.570667, // 지도의 중심 위도
        mapLevel: 3, // 지도의 확대 레벨
        markers: [], // 마커를 담을 배열
        keyword: '광주 북구 맛집',
        map: '',

      }
    },
    mounted(){
      this.mapContainer = document.getElementById('map')
      this.map = this.createMap(this.mapCenterY, this.mapCenterX)

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

      // 키워드 검색을 요청하는 함수
      searchplaces() {

        // 장소 검색 객체 생성
        let ps = new kakao.maps.services.Places()

        if (!this.keyword.replace(/^\s+|\s+$/g, '')) {
          alert('키워드를 입력해주세요!')
          return false
        }

        // 장소검색 객체를 통해 키워드로 장소검색을 요청
        ps.keywordSearch(keyword, this.placesSearchCB)

      },

      // 장소검색이 완료됐을 때 호출되는 콜백함수
      placesSearchCB(data, status, pagination) {
        if (status === kakao.maps.services.Status.OK) {

          // 정상적으로 검색이 완료되면, 검색 목록과 마커를 표출
          this.displayPlaces(data)

          // 페이지 번호를 표출
          this.displayPagination(pagination)
        } else if (status === kakao.maps.services.Status.ZERO_RESULT) {

            alert('검색 결과가 존재하지 않습니다.')
            return

        } else if (status === kakao.maps.services.Status.ERROR) {

          alert('검색 결과 중 오류가 발생했습니다.')
          return
        }
      },
      
      // 검색 결과 목록과 마커를 표출하는 함수
      displayPlaces(places) {

        // 검색 결과 목록이나 마커를 클릭했을 때 장소명을 표출할 인포윈도우를 생성
        let infowindow = new kakao.maps.InfoWindow({zIndex:1})

        let listEl = document.getElementById('placesList'),
        menuEl = document.getElementById('menu_wrap'),
        fragment = document.createDocumentFragment(),
        bounds = new kakao.maps.LatLngBounds(),
        listStr = ''

        // 검색 결과 목록에 추가된 항목들을 제거
        this.removeAllChildNods(listEl)

        // 지도에 표시되고 있는 마커 제거
        this.removeMarker()

        for ( let i=0; i<places.length; i++) {

          // 마커를 생성하고 지도에 표시
          let placePosition = new kakao.maps.LatLng(places[i].y, places[i].x),
          marker = this.addMarker(placePosition, i),
          itemEl = this.getListItem(i, places[i]) // 검색 결과 항목 Element를 생성

          // 검색된 장소 위치를 기준으로 지도 범위를 재설정하기 위헤
          // LatLngBounds 객체에 좌표를 추가
          bounds.extend(placePosition)

          // 마커와 검색결과 항목에 mouseover 했을때
          // 해당 장소를 인포윈도우에 장소명을 표시
          // mouseout 했을 때는 인포윈도우를 닫음
          (function(marker, title) {
            kakao.maps.event.addListener(marker, 'mouseover', function() {
              this.displayInfowindow(markers, title)
            })

            kakao.maps.event.addListener(marker, 'mouseout', function() {
              infowindow.close()
            })

            itemEl.onmouseover = function() {
              this.displayInfowindow(marker, title)
            }

            itemEl.onmouseout = function () {
              infowindow.close()
            }
          })(marker, places[i].place_name)

          fragment.appendChild(itemEl)
        }

        // 검색결과 항목들을 검색결과 목록 Element에 추가
        listEl.appendChild(fragment)
        menuEl.scrollTop = 0

        // 검색된 장소 위치를 기준으로 지도 범위를 재설정
        this.map.setBounds(bounds)
      },

      // 검색결과 항목을 Element로 반환하는 함수
      getListItem(index, places) {},

      // 마커를 생성하고 지도 위에 마커를 표시하는 함수
      addMarker(position, idx, title) {},

      // 지도 위에 표시되고 있는 마커를 모두 제거하는 함수
      removeMarker() {},

      // 검색결과 목록 하단에 페이지번호를 표시하는 함수
      displayPagination(pagination) {},

      // 검색결과 목록 또는 마커를 클릭했을 때 호출되는 함수
      // 인포윈도우에 장소명을 표시
      displayInfowindow(marker, title) {},

      // 검색결과 목록의 자식 Element를 제거하는 함수
      removeAllChildNods(el) {}
    },
  }
</script>
<style lang="stylus">
  #map
    width 100%
    height 600px
    position relative
    overflow hidden
</style>