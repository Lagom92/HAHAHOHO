<template>
  <div>
    <TopBanner></TopBanner>
    <v-container>
      <div>
        <v-card height="400px">
          <v-card-title class="justify-center" color="#F3B749">
            모임 목록
            <v-btn text icon to="/list">
              <v-icon color="#F3B749">
                mdi-plus-circle
              </v-icon>
            </v-btn>
          </v-card-title>
          <v-divider class="mx-4" inset></v-divider>
            <!-- 모임 관련 내용 -->
            <v-card-text 
              v-for="post in this.posts" 
              :key="post.id" 
              class="text--primary"
              xs12 
              sm6 
              md4>
              제목: {{post.title}}
              <!-- 이동 버튼 -->
              <v-btn :to="'/list/detail/' + post.id">go!</v-btn>
            </v-card-text>
        </v-card>
      </div>
      <v-row>
        <v-col cols="12" md="6">
          <v-card height="400px">
            <v-card-title class="justify-center" color="#F3B749">
              공지사항
              <v-btn text icon to="/board">
                <v-icon color="#F3B749">
                  mdi-plus-circle
                </v-icon>
              </v-btn>
            </v-card-title>
            <v-divider class="mx-4" inset></v-divider>
            <!-- 공지사항 관련 내용 -->
            <v-card-text 
              v-for="notice in this.notices" 
              :key="notice.id" 
              class="text--primary"
              xs12 
              sm6 
              md4>
              제목: {{notice.title}} <br/>
              내용: {{notice.contents}}
              <!-- 이동 버튼 -->
              <v-btn :to="'/notice/' + notice.id">go!</v-btn>
            </v-card-text>
          </v-card>
        </v-col>
        <v-col cols="12" md="6">
          <v-card height="400px">
            <v-card-title class="justify-center" color="#F3B749">
              자유게시판
              <v-btn text icon to="/board">
                <v-icon color="#F3B749">
                  mdi-plus-circle
                </v-icon>
              </v-btn>
            </v-card-title>
            <v-divider class="mx-4" inset></v-divider>
            <!-- 자유 게시판 관련 내용 -->
            <v-card-text 
              v-for="free in this.frees" 
              :key="free.id" 
              class="text--primary"
              xs12 
              sm6 
              md4>
              글 제목: {{free.title}}
            </v-card-text>
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
          <v-btn text>하하호호 자세히보기
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
      frees: []
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
</style>
