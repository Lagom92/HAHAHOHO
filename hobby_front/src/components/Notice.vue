<template>
  <div>
    <section id='top'>
      <h1 class="mb-3">공지사항</h1>
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
      <div v-for="post in posts" :key="post.id">
        <p>
          <v-row>
            <v-col cols='2'>{{post.id}}</v-col>
            <v-col cols='6'>{{post.title}}</v-col>
            <v-col cols='2'>{{post.created_at}}</v-col>
            <v-col cols='2'>{{post.name}}</v-col>
            <v-btn :to="'/notice/' + post.id">go</v-btn>
          </v-row>
        </p>
        <v-divider class='middivider' v-if="post % 3 == 0"></v-divider>
        <v-divider v-else></v-divider>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'Notice',
  data () {
    return {
      posts: []
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
