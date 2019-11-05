<template>
  <div>
    <section id='top'>
      <v-row class="px-3" align="center">
        <h1 class="mb-3 gamjaFont">자유게시판</h1>
        <v-spacer></v-spacer>
        <v-btn
        text 
        icon
        to= "/createfreeboard"
        v-if="user !== ''"
        >
          <v-icon color="#74b4a0">mdi-pencil-plus</v-icon>
        </v-btn>
      </v-row>
      <v-divider id='topdivider'></v-divider>
      <v-row class="d-none d-md-flex font-weight-black px-3">
        <v-col cols='2'>번호</v-col>
        <v-col cols='6'>내용</v-col>
        <v-col cols='2'>작성일시</v-col>
        <v-col cols='2'>작성자</v-col>
      </v-row>
      <v-row class="d-flex d-md-none font-weight-black px-3">
        <v-col cols='8'>내용</v-col>
        <v-col cols='4'>작성자</v-col>
      </v-row>
    </section>
    <v-divider class='middivider'></v-divider>
    <section id='content'>
      <div v-for="post in paginatedData" :key="post.id">
        <v-btn
          text
          block
          height="auto"
          :to="'/free/' + post.id"
        > 
          <v-row class="d-none d-md-flex px-3">
            <v-col cols='2'>{{post.id}} </v-col>
            <v-col cols='6'>{{post.title}}</v-col>
            <v-col cols='2'>{{post.created_at}} </v-col>
            <v-col cols='2'>{{post.username}}</v-col>
          </v-row>
          <v-row class="d-flex d-md-none px-3">
            <v-col cols='8' class="text-truncate">{{post.title}}</v-col>
            <v-col cols='4'>{{post.username}}</v-col>
          </v-row>
        </v-btn>
        <v-divider class='middivider' v-if="post % 3 == 0"></v-divider>
        <v-divider v-else></v-divider>
      </div>
    </section>
    <div class="text-center my-5">
        <v-pagination v-model="pageNum" :length="this.size" color="#74B4A0"></v-pagination>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FreeBoard',
  props: {
    pageSize: { type: Number, required: false, default: 6 }
  },
  data () {
    return {
      posts: [],
      pageNum: 1,
      size: null,
      user: this.$store.state.user_id
    }
  },
  computed: {
    paginatedData() {
      const start = (this.pageNum - 1) * this.pageSize,
            end = start + this.pageSize
      return this.posts.slice(start, end)
    }
  },
  mounted () {
    this.getFrees();
  },
  methods: {
    getFrees: function () {
      const baseUrl = this.$store.state.baseUrl
      const apiUrl = baseUrl + 'boards/free'
      this.$http.get(apiUrl)
        .then(res => {
          this.posts = res.data
          for (let i of res.data){
            i.created_at = String(i.created_at).substring(0,10)
          }

          let listLength = this.posts.length,
              listSize = this.pageSize,
              page = Math.floor((listLength - 1) / listSize) + 1
              this.size = page
        })
        .catch(err => {
          console.log(err)
        })
    },
  }  
}

</script>

<style lang="stylus">
#topdivider
  border-top-width 2px
  border-top-color #000

.middivider
  border-top-width 2px
</style>
