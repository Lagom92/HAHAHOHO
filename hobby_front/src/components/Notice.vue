<template>
  <div>
    <section id='top'>
      <h1 class="mb-3 gamjaFont">공지사항</h1>
      <v-divider id='topdivider'></v-divider>
      <v-row class="d-none d-md-flex font-weight-black px-3">
        <v-col cols="2">번호</v-col>
        <v-col cols="6">제목</v-col>
        <v-col cols="2">작성일시</v-col>
        <v-col cols="2">작성자</v-col>
      </v-row>
      <v-row class="d-flex d-md-none font-weight-black px-3">
        <v-col cols="8">제목</v-col>
        <v-col cols="4">작성자</v-col>
      </v-row>
    </section>
    <v-divider class='middivider'></v-divider>
    <section id='content'>
      <div v-for="post in paginatedData" :key="post.id">
        <v-btn
        text
        block
        height="auto"
        :to="'/notice/' + post.id"
        >
          <v-row class="d-none d-md-flex px-3">
            <v-col cols="2">{{post.id}}</v-col>
            <v-col cols="6">{{post.title}}</v-col>
            <v-col cols="2">{{post.created_at}}</v-col>
            <v-col cols="2">{{post.name}}</v-col>
          </v-row>
          <v-row class="d-flex d-md-none px-3">
            <v-col cols="8" class="text-truncate">{{post.title}}</v-col>
            <v-col cols="4">{{post.name}}</v-col>
          </v-row>
        </v-btn>
        <v-divider class='middivider' v-if="post % 3 == 0"></v-divider>
        <v-divider v-else></v-divider>
      </div>
    </section>
    <div class="text-center my-5">
        <v-pagination
        :length="this.size"
        v-model="pageNum"
        color="#74B4A0"
        ></v-pagination>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Notice',
  props: {
    pageSize: { type: Number, required: false, default: 6 }
  },
  data () {
    return {
      posts: [],
      pageNum: 1,
      size: null
    }
  },
  mounted () {
    this.getNotice()
  },
  computed: {
    paginatedData () {
      const start = (this.pageNum - 1) * this.pageSize
      const end = start + this.pageSize
      return this.posts.slice(start, end)
    }
  },
  methods: {
    getNotice: function () {
      const baseUrl = this.$store.state.base_url
      const apiUrl = baseUrl + 'boards/notice'
      this.$http.get(apiUrl)
        .then(res => {
          this.posts = res.data
          for (let i of res.data) {
            i.created_at = String(i.created_at).substring(0, 10)
          }

          let listLength = this.posts.length
          let listSize = this.pageSize
          let page = Math.floor((listLength - 1) / listSize) + 1
          this.size = page
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>

<style lang="stylus">
#topdivider
  border-top-width 2px
  border-top-color #000

.middivider
  border-top-width 2px

#cursorHand
  cursor pointer
</style>
