<template>
  <div>
    <TopBanner></TopBanner>
    <v-container>
      <div>
        <v-card class="pa-3" elevation="0" color="#fafafa">
          <v-card-title class="justify-center">
            모임 목록
            <v-btn text icon to="/list" class="ml-3">
              <v-icon color="#74b4a0">
                mdi-plus-circle
              </v-icon>
            </v-btn>
          </v-card-title>
          <!-- 모임 관련 내용 (WEB) -->
          <v-slide-group
            class="my-4 d-none d-sm-flex"
            show-arrows
          >
            <v-slide-item
              v-for="post in this.posts"
              :key="post.id"
            >
              <v-card
                class="ma-2"
                height="280"
                width="280"
                :to="'/list/detail/' + post.id"
              >
                <v-img
                  :src="post.photo"
                  class="white--text align-end mb-5"
                  gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                  height="280px"
                >
                  <v-card-title v-text="post.title"></v-card-title>
                </v-img>
              </v-card>
            </v-slide-item>
          </v-slide-group>
          <!-- 모임 관련 내용 (MOBILE) -->
          <v-carousel
            class="my-4 d-sm-none"
            :show-arrows="false"
            hide-delimiter-background
            delimiter-icon="mdi-minus"
            height="310"
          >
            <v-carousel-item
              v-for="post in this.posts"
              :key="post.id"
            >
              <v-card
                class="mx-auto"
                height="300"
                width="300"
                :to="'/list/detail/' + post.id"
              >
                <v-img
                  :src="post.photo"
                  class="white--text align-top"
                  gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                  height="300px"
                >
                  <v-card-title v-text="post.title"></v-card-title>
                </v-img>
              </v-card>
            </v-carousel-item>
          </v-carousel>
        </v-card>
      </div>
      <v-row>
        <v-col cols="12" md="6">
          <v-card class="pa-5" height="400px" elevation="0" color="#fafafa">
            <v-card-title class="justify-center">
              공지사항
              <v-spacer></v-spacer>
              <v-btn text icon to="/board">
                <v-icon color="#74b4a0">
                  mdi-plus-circle
                </v-icon>
              </v-btn>
            </v-card-title>
            <v-divider class="titleDiv"></v-divider>
            <!-- 공지사항 관련 내용 -->
            <div
              v-for="notice in this.notices"
              :key="notice.id"
            >
              <v-btn
                text
                block
                height="auto"
                :to="'/notice/' + notice.id"
              >
                <v-row class="my-2" justify="center">
                  <v-icon cols="1" small color="#EE7785">mdi-water</v-icon>
                  <v-col cols="7" class="text-truncate">{{notice.title}}</v-col>
                  <v-col cols="3" class="text-center">{{notice.created_at}}</v-col>
                </v-row>
              </v-btn>
              <v-divider></v-divider>
            </div>
          </v-card>
        </v-col>
        <v-col cols="12" md="6">
          <v-card class="pa-5" height="400px" elevation="0" color="#fafafa">
            <v-card-title class="justify-center">
              자유게시판
              <v-spacer></v-spacer>
              <v-btn text icon to="/board">
                <v-icon color="#74b4a0">
                  mdi-plus-circle
                </v-icon>
              </v-btn>
            </v-card-title>
            <v-divider class="titleDiv"></v-divider>
            <!-- 자유 게시판 관련 내용 -->
            <div
              v-for="free in this.frees"
              :key="free.id"
            >
              <v-btn
                text
                block
                height="auto"
                :to="'/free/' + free.id"
              >
                <v-row class="my-2" justify="center">
                  <v-icon cols="2" small color="#EE7785">mdi-water</v-icon>
                  <v-col cols="7" class="text-truncate">{{free.title}}</v-col>
                  <v-col cols="3" class="text-center">{{free.created_at}}</v-col>
                </v-row>
              </v-btn>
              <v-divider></v-divider>
            </div>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
    <v-card class="intro">
      <div id="cardcontent">
        <v-card-title class="headline justify-center">
          하하호호 하비하비 호비호비
        </v-card-title>
        <v-card-text class="text-center">
          안녕하세요. 즐거운 취미생활을 즐겨보아요~~ 저희가 더 궁금하시다면?
          <v-btn text to="/about">
            하하호호 자세히보기
            <v-icon color="#F3B749">mdi-arrow-right-bold</v-icon>
          </v-btn>
        </v-card-text>
      </div>
    </v-card>
  </div>
</template>

<script>
import TopBanner from '../components/TopBanner'

export default {
  name: 'Home',
  components: {
    TopBanner
  },
  data () {
    return {
      jwt: '',
      posts: [],
      notices: [],
      frees: [],

    }
  },
  mounted () {
    this.getJwt()
    this.getHobby()
    this.getNotice()
    this.getFree()
  },
  methods: {
    getJwt () {
      if (this.$route.query.jwt) {
        // 네이버 로그인 시 jwt가 여기서 날아오기 때문에 store에 저장하기
        this.jwt = this.$route.query.jwt
      }
    },
    getHobby: function () {
      const baseUrl = this.$store.state.baseUrl
      const apiUrl = baseUrl + 'boards/main/hobby'
      this.$http.get(apiUrl)
        .then(res => {
          this.posts = res.data 
        })
        .catch(err => {
          console.log(err)
        })
    },
    getNotice: function () {
      const baseUrl = this.$store.state.baseUrl
      const apiUrl = baseUrl + 'boards/main/notice'
      this.$http.get(apiUrl)
        .then(res => {
          for (let i of res.data){
            i.created_at = String(i.created_at).substring(0,10)
          }
          this.notices = res.data 
        })
        .catch(err => {
          console.log(err)
        })
    },
    getFree: function () {
      const baseUrl = this.$store.state.baseUrl
      const apiUrl = baseUrl + 'boards/main/free'
      this.$http.get(apiUrl)
        .then(res => {
          for (let i of res.data){
            i.created_at = String(i.created_at).substring(0,10)
          }
          this.frees = res.data 
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>

<style lang="stylus">
.intro
  position relative
  height 30vh
  background-color #f2f2f2
  margin-bottom 50px

#cardcontent
  position relative
  top 20%

.text-truncate
  width 200px

.titleDiv
  border-top-width 3px
</style>
