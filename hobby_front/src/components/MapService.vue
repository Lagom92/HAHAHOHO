<template>
    <v-container>
      <div class="map_wrap">
        <div id="map"></div>

        <div id="menu_wrap" class="bg_white" v-show="searchService && searchWindow">
          <div class="option">
            <div class="d-flex">
              <v-text-field
                class="mx-3"
                v-model="keyword"
                :counter="15"
                label="키워드"
                @keydown.enter="searchPlaces"
              ></v-text-field>
              <v-btn
                class="align-self-center px-2 mr-2"
                outlined
                color="blue-grey"
                @click="searchPlaces"
              >검색하기</v-btn>
            </div>
          </div>
          <hr>
          <ul id="placesList" class="pl-0"></ul>
          <div id="pagination"></div>
        </div>

        <div v-show="searchService && !searchWindow" @click="openSearch">
          <v-btn id="menu_btn"><v-icon>mdi-magnify</v-icon></v-btn>
        </div>
      </div>
    </v-container>
</template>

<script>
export default {
  name: 'MapService',
  data(){
    return {
      mapContainer: '', // 지도를 표시할 div
      markers: [], // 마커를 담을 배열
      keyword: '', // 검색 키워드
      map: '', // 지도 객체
      infowindow: '', // 검색 결과 목록이나 마커를 클릭했을 때 장소명을 표출할 인포윈도우
      ps: '', // 장소 검색 객체 생성
      searchWindow: false, // 장소 검색창 열림유무
      mainMarker: '', // 마커 객체
      markerInfo: '' // 마커 위치 정보
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
    this.map = this.createMap(this.mapCenterY, this.mapCenterX)
    this.infowindow = new kakao.maps.InfoWindow({zIndex:1})
    this.ps = new kakao.maps.services.Places()
    this.mainMarker = new kakao.maps.Marker()
    this.createMarker(this.mapCenterX, this.mapCenterY)
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

      // 마커가 표시될 위치
      let markerPosition = new kakao.maps.LatLng(y, x)
      this.mainMarker.setPosition(markerPosition)

      // 마커를 지도 위에 표시
      this.mainMarker.setMap(this.map)

      // 마커 드래그 기능 사용 유무
      this.mainMarker.setDraggable(this.searchService)

      // 마커 위에 정보 표시
      await this.coord2address(x, y)
      this.displayInfowindow(this.mainMarker, this.markerInfo)
    },

    // 좌표를 상세 주소로 변경하는 함수
    async coord2address(x, y) {
      await this.$http.get('https://dapi.kakao.com/v2/local/geo/coord2address.json', {
        params: {
          x: x,
          y: y
        },
        headers: {
          Authorization: 'KakaoAK ' + process.env.VUE_APP_REST
        }
      }).then( res => {
          if (res.data.documents[0].road_address.building_name) {
            this.markerInfo = res.data.documents[0].road_address.building_name
          } else {
            this.markerInfo = res.data.documents[0].road_address.address_name
          }
      }).catch( e => {
          console.log(e)
      })
    },

    // 키워드 검색을 요청하는 함수
    searchPlaces() {

      if (!this.keyword.replace(/^\s+|\s+$/g, '')) {
        alert('키워드를 입력해주세요!')
        return false
      }

      // 장소검색 객체를 통해 키워드로 장소검색을 요청
      this.ps.keywordSearch(this.keyword, this.placesSearchCB)
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

      let listEl = document.getElementById('placesList')
      let menuEl = document.getElementById('menu_wrap')
      let fragment = document.createDocumentFragment()
      let bounds = new kakao.maps.LatLngBounds()
      let listStr = ''

      // 검색 결과 목록에 추가된 항목들을 제거
      this.removeAllChildNods(listEl)

      // 지도에 표시되고 있는 마커 제거
      this.removeMarker()

      for ( let i = 0; i < places.length; i++) {

        // 마커를 생성하고 지도에 표시
        let placePosition = new kakao.maps.LatLng(places[i].y, places[i].x)
        let marker = this.addMarker(placePosition, i)
        let itemEl = this.getListItem(i, places[i]) // 검색 결과 항목 Element를 생성

        // 검색된 장소 위치를 기준으로 지도 범위를 재설정하기 위헤
        // LatLngBounds 객체에 좌표를 추가
        bounds.extend(placePosition);

        // 마커와 검색결과 항목에 mouseover 했을때
        // 해당 장소를 인포윈도우에 장소명을 표시
        // mouseout 했을 때는 인포윈도우를 닫음
        (function(title, infowindow, displayInfowindow, map, closeSearch, searchWindow) {

          let oneBound = new kakao.maps.LatLngBounds()
          oneBound.extend(placePosition)

          kakao.maps.event.addListener(marker, 'mouseover', function() {
            displayInfowindow(marker, title)
          })

          kakao.maps.event.addListener(marker, 'mouseout', function() {
            infowindow.close()
          })

          kakao.maps.event.addListener(marker, 'click', function() {
            map.setBounds(oneBound)
            closeSearch(placePosition)
            displayInfowindow(marker, title)
          })

          itemEl.onmouseover = function() {
            map.setBounds(bounds)
            displayInfowindow(marker, title)
          }

          itemEl.onmouseout = function() {
            infowindow.close()
          }

          itemEl.onclick = function() {
            map.setBounds(oneBound)
            closeSearch(placePosition)
            displayInfowindow(marker, title)
          }
        })(places[i].place_name, this.infowindow, this.displayInfowindow, this.map, this.closeSearch, this.searchWindow);

        fragment.appendChild(itemEl)
      }

      // 검색결과 항목들을 검색결과 목록 Element에 추가
      listEl.appendChild(fragment)
      menuEl.scrollTop = 0

      // 검색된 장소 위치를 기준으로 지도 범위를 재설정
      this.map.setBounds(bounds)
    },

    // 검색결과 항목을 Element로 반환하는 함수
    getListItem(index, places) {

      let el = document.createElement('li')
      let itemStr = '<span class="markerbg marker_' + (index+1) + '"></span>' +
                '<div class="mapinfo">' +
                '   <h5>' + places.place_name + '</h5>'

      if (places.road_address_name) {
        itemStr += '    <span>' + places.road_address_name + '</span>' +
                    '   <span class="jibun gray">' +  places.address_name  + '</span>';
      } else {
        itemStr += '    <span>' +  places.address_name  + '</span>'
      }

      itemStr += '  <span class="tel">' + places.phone  + '</span>' + '</div>'

      el.innerHTML = itemStr
      el.className = 'item'

      return el
    },

    // 마커를 생성하고 지도 위에 마커를 표시하는 함수
    addMarker(position, idx, title) {

      // 마커 이미지 url, 스프라이트 이미지를 씀
      let imageSrc = 'http://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_number_blue.png'
      let imageSize = new kakao.maps.Size(36, 37) // 마커 이미지 크기
      let imgOptions = {
        spriteSize: new kakao.maps.Size(36, 691), // 스프라이트 이미지의 크기
        spriteOrigin: new kakao.maps.Point(0, (idx*46)+10), // 스프라이트 이미지 중 사용할 영역의 좌상단 좌표
        offset: new kakao.maps.Point(13, 37) // 마커 좌표에 일치시킬 이미지 내에서의 좌표
      }
      let markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imgOptions)
      let marker = new kakao.maps.Marker({
        position: position, // 마커 위치
        image: markerImage
      })

      marker.setMap(this.map) // 지도 위에 마커를 표출
      this.markers.push(marker) // 배열에 생성된 마커를 추가

      return marker
    },

    // 지도 위에 표시되고 있는 마커를 모두 제거하는 함수
    removeMarker() {

      for (let i = 0; i < this.markers.length; i++) {
        this.markers[i].setMap(null)
      }
      this.markers = []
    },

    // 검색결과 목록 하단에 페이지번호를 표시하는 함수
    displayPagination(pagination) {
      
      let paginationEl = document.getElementById('pagination')
      let fragment = document.createDocumentFragment()

      // 기존에 추가된 페이지번호를 삭제
      while (paginationEl.hasChildNodes()) {
        paginationEl.removeChild(paginationEl.lastChild)
      }

      for (let i = 1; i <= pagination.last; i++) {
        let el = document.createElement('a')
        el.href = '#'
        el.innerHTML = i

        if (i === pagination.current) {
          el.className = 'on'
        } else {
          el.onclick = (function(i) {
            return function() {
              pagination.gotoPage(i)
            }
          })(i)
        }

        fragment.appendChild(el)
      }
      paginationEl.appendChild(fragment)
    },

    // 검색결과 목록 또는 마커를 클릭했을 때 호출되는 함수
    // 인포윈도우에 장소명을 표시
    displayInfowindow(marker, title) {
      let content = '<div id="info_window">' + title + '</div>'

      this.infowindow.setContent(content)
      this.infowindow.open(this.map, marker)
    },

    // 검색결과 목록의 자식 Element를 제거하는 함수
    removeAllChildNods(el) {
      while (el.hasChildNodes()) {
        el.removeChild(el.lastChild)
      }
    },

    // 검색창 여닫기
    closeSearch(latlng) {
      this.mapCenterY = latlng.Ha
      this.mapCenterX = latlng.Ga
      this.createMarker(latlng.Ga, latlng.Ha)
      this.searchWindow = false
    },
    openSearch() {
      this.mainMarker.setMap(null)
      this.infowindow.close()
      this.searchWindow = true
    }
  },
}
</script>
<style lang="stylus">

  #info_window
    padding 5px
    z-index 1

  #menu_btn
    position absolute
    top 1rem
    left 1rem
    z-index 1

  #map
    width 100%
    height 30rem
    position relative
    overflow hidden
  
  .map_wrap .map_wrap *
    margin 0
    padding 0
    font-family 'Malgun Gothic' dotum '돋움' sans-serif
    font-size 12px
  
  .map_wrap a .map_wrap a:hover .map_wrap a:active
    color #000
    text-decoration none

  .map_wrap
    position relative
    width 100%
    height 30rem
  
  #menu_wrap
    position absolute
    top 0
    left 0
    bottom 0
    width 18rem
    margin 10px 10px 30px 10px
    padding 5px
    overflow-y auto
    background rgba(255, 255, 255, 0.8)
    z-index 1
    font-size 12px
    border-radius 10px
  
  .bg_white
    background #fff

  #menu_wrap hr
    display block
    height 1px
    border 0
    border-top 2px solid #5F5F5F
    margin 3px 0
    
  #menu_wrap .option
    text-align center
  
  #menu_wrap .option p
    margin 10px 0

  #menu_wrap .option button
    margin-left 5px

  #placesList li
    list-style none

  #placesList .item
    position relative
    border-bottom 1px solid #888
    overflow hidden
    cursor pointer
    min-height 65px

  #placesList .item span
    display block
    margin-top 4px

  #placesList .item h5, #placesList .item .mapinfo
    text-overflow ellipsis
    overflow hidden
    white-space nowrap

  #placesList .item .mapinfo
    padding 10px 0 10px 55px

  #placesList .mapinfo .gray
    color #8a8a8a

  #placesList .mapinfo .jibun
    padding-left 26px
    background url(http://t1.daumcdn.net/localimg/localimages/07/mapapidoc/places_jibun.png) no-repeat

  #placesList .mapinfo .tel
    color #009900

  #placesList .item .markerbg
    float left
    position absolute
    width 36px
    height 37px
    margin 10px 0 0 10px
    background url(http://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_number_blue.png) no-repeat

  #placesList .item .marker_1
    background-position 0 -10px

  #placesList .item .marker_2
    background-position 0 -56px

  #placesList .item .marker_3
    background-position 0 -102px

  #placesList .item .marker_4
    background-position 0 -148px

  #placesList .item .marker_5
    background-position 0 -194px

  #placesList .item .marker_6
    background-position 0 -240px

  #placesList .item .marker_7
    background-position 0 -286px

  #placesList .item .marker_8
    background-position 0 -332px

  #placesList .item .marker_9
    background-position 0 -378px

  #placesList .item .marker_10
    background-position 0 -423px

  #placesList .item .marker_11
    background-position 0 -470px

  #placesList .item .marker_12
    background-position 0 -516px

  #placesList .item .marker_13
    background-position 0 -562px

  #placesList .item .marker_14
    background-position 0 -608px

  #placesList .item .marker_15
    background-position 0 -654px

  #pagination
    margin 0px auto
    text-align center

  #pagination a
    display inline-block
    margin-right 10px
    font-size medium
    text-decoration none

  #pagination .on
    font-weight bold
    cursor default
    color #777
</style>