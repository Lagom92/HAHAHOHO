<template>
  <v-container>
    <v-flex class="pa-7">
      <div>
        <h1>{{post.title}}</h1>
        <v-row class="px-3">
          <p color="grey lighten-1">{{post.created_at}}</p>
          <v-spacer></v-spacer>
          <span>조회수: 0</span>
        </v-row>
      </div>
      <v-divider class="minDiv mb-5"></v-divider>
      <div>
        <div>
          <xmp>{{post.contents}}</xmp>
          <br/>
        </div>
        <v-divider class="minDiv mb-5"></v-divider>
        <div class="d-flex justify-end">
          <v-btn dark :to="'/board'" color="#74B4A0">목록으로</v-btn>
        </div>
      </div>
    </v-flex>
  </v-container>
</template>

<script>
export default {
  name: 'NoticeDetail',
  data () {
    return {
      post: {}
    }
  },
  mounted () {
    this.id = this.$route.params.id
    this.getDetail()
  },
  methods: {
    getDetail () {
      const baseUrl = this.$store.state.base_url
      const apiUrl = baseUrl + 'boards/notice/' + this.id
      this.$http.get(apiUrl)
        .then(res => {
          let createdAt = res.data.created_at
          res.data.created_at = createdAt.substring(0, 4) + '년 ' +
                                createdAt.substring(5, 7) + '월 ' +
                                createdAt.substring(8, 10) + '일'
          this.post = res.data
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>

<style lang="stylus">
xmp
  white-space pre-wrap
  word-wrap break-word

.minDiv
  border-top-width 2px
</style>
