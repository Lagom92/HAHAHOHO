<template>
  <v-container>
    <v-flex class="pa-7">
      <div>
        <h1 class="my-3">{{post.title}}</h1>
          <v-row class="px-3">
            <p class="borderP">{{post.created_at}}</p>
            <p>{{post.username}}</p>
            <v-spacer></v-spacer>
            <p class="borderP">조회수: 0</p>
            <p>댓글수: 0</p>
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
          <v-btn
          v-if="user === post.user"
          @click="$router.push({ name: 'updatefreeboard', params: { id: post.id }})"
          class="mr-3"
          color="light-blue"
          dark
          >
            수정
          </v-btn>
          <v-btn
          v-if="user === post.user"
          @click="deleteDetail()"
          class="mr-3"
          color="pink"
          dark
          >
            삭제
          </v-btn>
          <v-btn to= "/board" color="#74B4A0" dark>
            목록으로
          </v-btn>
        </div>
      </div>
      <Comment class="mt-10"></Comment>
    </v-flex>
  </v-container>
</template>

<script>
import Comment from '@/components/Comment'

export default {
  name: 'FreeBoardDetail',
  components: {
    Comment
  },
  data () {
    return {
      post: {},
      user: this.$store.state.user_id
    }
  },
  mounted () {
    this.id = this.$route.params.id
    this.getDetail()
  },
  methods: {
    getDetail () {
      const baseUrl = this.$store.state.baseUrl
      const apiUrl = baseUrl + 'boards/free/' + this.id
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
    },
    deleteDetail () {
      const baseUrl = this.$store.state.base_url
      const apiUrl = baseUrl + 'boards/free/' + this.id
      this.$http.delete(apiUrl)
        .then(res => {
          this.$router.go(-1)
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
