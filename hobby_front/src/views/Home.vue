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
          <v-card class="pa-5" elevation="0" color="#fafafa">
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
                  <v-col cols="7" class="subtitle-1 text-truncate">{{notice.title}}</v-col>
                  <v-col cols="3" class="subtitle-1 text-center">{{notice.created_at}}</v-col>
                </v-row>
              </v-btn>
              <v-divider></v-divider>
            </div>
          </v-card>
        </v-col>
        <v-col cols="12" md="6">
          <v-card class="pa-5" elevation="0" color="#fafafa">
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
                  <v-col cols="7" class="subtitle-1 text-truncate">{{free.title}}</v-col>
                  <v-col cols="3" class="subtitle-1 text-center">{{free.created_at}}</v-col>
                </v-row>
              </v-btn>
              <v-divider></v-divider>
            </div>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
    <v-card class="intro">
      <v-img
        src="https://cdn.pixabay.com/photo/2019/10/23/16/36/black-4572125_960_720.jpg"
        class="white--text align-center"
        gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
        height="100%"
      >
        <v-card-title class="display-1 justify-center">
          하하호호에 처음 오셨나요?
        </v-card-title>
        <v-card-text class="text-center">
          <div class="title font-weight-thin">하하호호는 건전한 취미생활, 밝은 에너지, 신뢰있는 관계를 통해 서비스를 운영하고 있습니다.</div>
          <div class="title font-weight-thin">저희 사이트에 대한 소개를 읽어봐주세요^^</div>
          <v-btn dark large to="/about" color="#EE7785">
            하하호호 알아보기
            <v-icon class="ma-1">mdi-arrow-right-bold</v-icon>
          </v-btn>
        </v-card-text>
      </v-img>
    </v-card>
    <v-card class="intro">
      <v-card-title class="display-1 justify-center">
        하하호호의 소식을 빠르게 알고 싶나요?
      </v-card-title>
      <v-card-text class="text-center">
        <div class="title font-weight-thin">카카오 플러스 친구를 해보세요~</div>
        <v-btn dark large color="#EE7785">
          플러스친구 추가하기
          <v-icon>mdi-arrow-right-bold</v-icon>
        </v-btn>
      </v-card-text>
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
  height 40vh
  background-color #f2f2f2

.text-truncate
  width 200px

.titleDiv
  border-top-width 3px
</style>
