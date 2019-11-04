<template>
  <div>
    <section id='top'>
      <h1 class="mb-3 gamjaFont">공지사항</h1>
      <v-divider id='topdivider'></v-divider>
      <v-row class="font-weight-black">
        <v-col cols='2'>번호</v-col>
        <v-col cols='6'>제목</v-col>
        <v-col cols='2'>작성일시</v-col>
        <v-col cols='2'>작성자</v-col>
      </v-row>
    </section>
    <v-divider class='middivider'></v-divider>
    <section id='content'>
      <div v-for="post in paginatedData" :key="post.id">
        <router-link :to="'/notice/' + post.id">
          <v-row>
            <v-col cols='2'>{{post.id}}</v-col>
            <v-col cols='6'>{{post.title}}</v-col>
            <v-col cols='2'>{{post.created_at}}</v-col>
            <v-col cols='2'>{{post.name}}</v-col>
          </v-row>
        </router-link>
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
  computed: {
    paginatedData() {
      const start = (this.pageNum - 1) * this.pageSize,
            end = start + this.pageSize
      return this.posts.slice(start, end)
    }
  },
  mounted () {
    this.getNotice()
  },
  methods: {
    getNotice: function () {
      const baseUrl = this.$store.state.baseUrl
      const apiUrl = baseUrl + 'boards/notice'
      this.$http.get(apiUrl)
        .then(res => {
          this.posts = res.data

          let listLength = this.posts.length,
              listSize = this.pageSize,
              page = Math.floor((listLength - 1) / listSize) + 1
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
</style>
