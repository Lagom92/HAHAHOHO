<template>
  <div>
    <v-container>
      <SearchBar class="d-flex justify-center my-5"></SearchBar>
      <v-alert
      class="mt-5 mb-10"
      border='top'
      color="info"
      elevation="2"
      colored-border
      >
        <p class="mb-0 mt-3">검색키워드 : <strong>{{word}}</strong></p>
      </v-alert>
      <div class="mb-10">
        <v-row class="px-3">
          <h2>모임 검색결과 ({{cnt}})</h2>
          <v-spacer></v-spacer>
          <v-btn @click="$router.push('/list')" color="#EE7785" text>
            <v-icon>mdi-plus</v-icon>
            더보기
          </v-btn>
        </v-row>
        <v-divider class="minDiv my-3"></v-divider>
        <v-layout wrap>
          <v-flex v-for="post in this.posts" :key="post.id" xs12 sm6 md4>
            <v-card class="ma-3" :to="'/list/detail/' + post.id">
              <v-img :src="post.photo" height="200px"/>
              <v-card-title primary-title>
                <div class="headline">{{post.title}}</div>
              </v-card-title>
              <v-card-text>
                <p id="postContent" class="grey--text">{{post.contents}}</p>
              </v-card-text>
            </v-card>
          </v-flex>
          <!-- 검색 모임이 없는 경우 -->
          <p v-if="cnt===0">검색 결과가 없습니다.</p>
        </v-layout>
      </div>
      <div class="mb-10">
        <v-row class="px-3">
          <h2>자유게시판 검색결과 ({{cntF}})</h2>
          <v-spacer></v-spacer>
          <v-btn @click="$router.push('/board')" color="#EE7785" text>
            <v-icon>mdi-plus</v-icon>
            더보기
          </v-btn>
        </v-row>
        <v-divider class="minDiv my-3"></v-divider>
        <div>
          <v-row class="font-weight-black my-2">
            <v-col cols="8">내용</v-col>
            <v-col class="text-center" cols="2">작성일시</v-col>
            <v-col class="text-center" cols="2">작성자</v-col>
          </v-row>
          <div v-for="free in frees" :key="free.id">
            <v-row class="my-2">
              <v-col cols='8' class="rightBorder">
                <router-link
                id="postContent"
                tag="p"
                :to="'/free/' + free.id"
                text-color="black"
                >
                  {{free.contents}}
                </router-link>
              </v-col>
              <v-col class="rightBorder text-center" cols="2">
                {{free.created_at}}
              </v-col>
              <v-col class="text-center" cols="2">{{free.username}}</v-col>
            </v-row>
            <v-divider></v-divider>
          </div>
          <!-- 검색 모임이 없는 경우 -->
          <p v-if="cntF===0">검색 결과가 없습니다.</p>
        </div>
      </div>
    </v-container>
  </div>
</template>

<script>
import SearchBar from '../components/SearchBar'

export default {
  name: 'SearchPage',
  data () {
    return {
      word: '',
      posts: [],
      cnt: 0,
      frees: [],
      cntF: 0
    }
  },
  components: {
    SearchBar
  },
  mounted () {
    this.word = this.$store.state.search_word
    this.search()
  },
  methods: {
    search: function () {
      const baseUrl = this.$store.state.base_url
      const apiUrl = baseUrl + 'boards/hobby?q=' + this.word
      this.$http.get(apiUrl)
        .then(res => {
          this.cnt = res.data.length
          this.posts = res.data
        })
        .catch(err => {
          console.log(err)
        })

      const api = baseUrl + 'boards/free?q=' + this.word
      this.$http.get(api)
        .then(res => {
          this.cntF = res.data.length
          for (let i of res.data) {
            i.created_at = String(i.created_at).substring(0, 10)
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
#postContent
  overflow hidden
  text-overflow ellipsis
  white-space nowrap
  cursor pointer

.rightBorder
  border-right 1px solid rgba(0, 0, 0, 0.12)
</style>
