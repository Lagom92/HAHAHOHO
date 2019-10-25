<template>
  <div>
    <TopBanner></TopBanner>
    <v-container>
      <div>
        <v-card height="400px">
          <v-card-title class="justify-center" color="#F3B749">
            모임 목록
            <v-icon class="ml-3" color="#F3B749">
              mdi-plus-circle
            </v-icon>
          </v-card-title>
          <v-divider class="mx-4" inset></v-divider>
        </v-card>
      </div>
      <v-row>
        <v-col cols="12" md="6">
          <v-card height="400px">
            <v-card-title class="justify-center" color="#F3B749">
              공지사항
              <v-icon class="ml-3" color="#F3B749">
                mdi-plus-circle
              </v-icon>
            </v-card-title>
            <v-divider class="mx-4" inset></v-divider>
          </v-card>
        </v-col>
        <v-col cols="12" md="6">
          <v-card height="400px">
            <v-card-title class="justify-center" color="#F3B749">
              자유게시판
              <v-icon class="ml-3" color="#F3B749">
                mdi-plus-circle
              </v-icon>
            </v-card-title>
            <v-divider class="mx-4" inset></v-divider>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
    <v-card class="intro">
      <div id="cardcontent">
        <v-card-title class="headline justify-center">하하호호 하비하비 호비호비</v-card-title>
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
  data (){
    return{
      jwt:''
    }
  },
  mounted (){
    this.getJwt()
  },
  methods:{
    getJwt(){
      if(this.$route.query.jwt){
        // 네이버 로그인 시 jwt가 여기서 날아오기 때문에 store에 저장하기
        this.jwt = this.$route.query.jwt
      }
    }
  }
}
</script>

<style>
  .intro {
    position: relative;
    height: 30vh;
    background-color: #f2f2f2;
    margin-bottom: 50px;
  }
  #cardcontent {
    position: relative;
    top: 20%;
  }
</style>