<template>
  <div>
    <div class="mb-1">
      <v-card color="#fafafa" flat>
        <v-container v-if="user !== ''">
          <v-row class="createuser px-3" align="center">
            <div>작성자 : <span class="font-weight-black">{{user}}</span></div>
            <v-spacer></v-spacer>
            <v-btn @click="createComment()" color="primary" text icon>
              <v-icon>mdi-pencil</v-icon>
            </v-btn>
          </v-row>
          <v-text-field
          @keyup.enter="createComment()"
          v-model="word"
          label="댓글 작성"
          placeholder="주제와 무관한 댓글, 타인의 권리를 침해하거나 명예를 훼손하는 댓글은 별도의 통보 없이 재제를 받을 수 있습니다."
          outlined
          shaped
          ></v-text-field>
        </v-container>
      </v-card>
    </div>
    <div>
      <v-card
      v-for="(post, idx) in paginatedData"
      :key="post.id"
      color="#fafafa"
      flat
      >
        <v-container>
          <div>
            <v-row class="mx-0">
              <v-row class="createuser px-3" align="center">
                <div class="font-weight-black">{{post.name}}</div>
                <v-divider class="mx-5" vertical inset></v-divider>
                <div>{{post.created_at}}</div>
                <v-spacer></v-spacer>
                <v-btn
                v-if="userId === post.user"
                @click="deleteComment(post.id, idx)"
                text
                icon
                >
                  <v-icon color="error">mdi-trash-can-outline</v-icon>
                </v-btn>
              </v-row>
            </v-row>
            <p class="mb-0">{{post.contents}}</p>
          </div>
        </v-container>
        <v-divider></v-divider>
      </v-card>
      <div class="text-center my-5">
        <v-pagination :length="this.size" v-model="pageNum" color="#74B4A0">
        </v-pagination>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Comment',
  props: {
    pageSize: { type: Number, required: false, default: 6 }
  },
  data () {
    return {
      user: '',
      posts: [],
      word: '',
      userId: '',
      pageNum: 1,
      size: null
    }
  },
  mounted () {
    this.user = this.$store.state.user_name
    this.userId = this.$store.state.user_id
    this.id = this.$route.params.id
    this.getComments()
  },
  computed: {
    paginatedData () {
      const start = (this.pageNum - 1) * this.pageSize
      const end = start + this.pageSize
      return this.posts.slice(start, end)
    }
  },
  methods: {
    getComments () {
      const baseUrl = this.$store.state.base_url
      const apiUrl = baseUrl + 'boards/free/' + this.id + '/comments'
      this.$http.get(apiUrl)
        .then(res => {
          for (let i of res.data) {
            i.created_at = (
              String(i.created_at).substring(0, 10) + '  ' +
              String(i.created_at).substring(11, 16)
            )
          }
          this.posts = res.data
          let listLength = this.posts.length
          let listSize = this.pageSize
          let page = Math.floor((listLength - 1) / listSize) + 1
          this.size = page
        })
        .catch(err => {
          console.log(err)
        })
    },
    createComment () {
      const baseUrl = this.$store.state.base_url
      let form = new FormData()

      form.append('name', this.user)
      form.append('user', this.$store.state.user_id)
      form.append('postFree', this.id)
      form.append('contents', this.word)

      const apiUrl = baseUrl + 'boards/free/' + this.id + '/comment'
      this.$http.post(apiUrl, form)
        .then(res => {
          res.data.created_at = (
            String(res.data.created_at).substring(0, 10) + '  ' +
            String(res.data.created_at).substring(11, 16)
          )
          this.posts.unshift(res.data)
          this.word = ''
        })
        .catch(err => {
          console.log(err)
        })
    },
    deleteComment (id, idx) {
      const baseUrl = this.$store.state.base_url
      const apiUrl = baseUrl + 'boards/comment/' + id
      this.$http.delete(apiUrl)
        .then(res => {
          this.posts.splice(idx, 1)
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>

<style lang="stylus">
.borderP
  border-right 1px solid rgba(0, 0, 0, 0.12)
  padding-right 10px
  margin-right 10px

  .commentInput
    width 100%
</style>
