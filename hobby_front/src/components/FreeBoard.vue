<template>
  <div>
    <section id='top'>
      <v-row>
        <h1 class="mb-3">자유게시판</h1>
        <v-spacer></v-spacer>
        <v-btn 
        text 
        icon
        to= "/createfreeboard"
        >
          <v-icon>mdi-pencil-plus</v-icon>
        </v-btn>
      </v-row>
      <v-divider id='topdivider'></v-divider>
      <v-row class="font-weight-black">
        <v-col cols='8'>내용</v-col>
        <v-col cols='2'>작성일시</v-col>
        <v-col cols='2'>작성자</v-col>
      </v-row>
    </section>
    <v-divider class='middivider'></v-divider>
    <section id='content'>
      <div v-for="post in posts" :key="post.id">
        <a href="#">
          <v-row>
            <v-col cols='8'>{{post.title}}</v-col>
            <v-col cols='2'>{{post.created_at}} </v-col>
            <v-col cols='2'>{{post.username}}</v-col>
          </v-row>
        </a>
        <v-divider class='middivider' v-if="post % 3 == 0"></v-divider>
        <v-divider v-else></v-divider>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'FreeBoard',
  data () {
    return {
      posts: [],
    }
  },
  mounted () {
    this.get_frees();
  },
  methods: {
    get_frees: function () {
      const baseUrl = this.$store.state.baseUrl
      const apiUrl = baseUrl + 'boards/free'
      this.$http.get(apiUrl)
        .then(res => {
          this.posts = res.data 
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
