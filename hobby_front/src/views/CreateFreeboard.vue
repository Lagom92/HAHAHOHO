<template>
  <div>
    <v-container>
      <v-row>
        <v-col cols="12" md="8" offset-md="2">
          <div>
            <h1 class="gamjaFont">자유게시판 글쓰기</h1>
          </div>
          <v-divider></v-divider>
          <v-form ref="form" v-model="valid">
            <v-text-field
            v-model="title"
            :counter="30"
            label="글 제목"
            ></v-text-field>
            <v-textarea
            v-model="contents"
            label="글 내용"
            outlined
            ></v-textarea>
          </v-form>
          <v-row>
            <div class="ml-auto pa-2">
              <v-btn @click="createFree()" dark color="#74b4a0">
                등록하기
              </v-btn>
            </div>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  name: 'CreateFreeboard',
  data () {
    return {
      title: '',
      contents: '',
      valid: true
    }
  },

  methods: {
    createFree: function () {
      const baseUrl = this.$store.state.base_url
      let form = new FormData()

      form.append('title', this.title)
      form.append('contents', this.contents)
      form.append('user', this.$store.state.user_id)
      form.append('username', this.$store.state.user_name)
      form.append('post', 2) // 2 : 자유 게시판 Default
      const apiUrl = baseUrl + 'boards/free'

      this.$http.post(apiUrl, form)
        .then(res => {
          this.$router.push({ path: 'board', props: { poropsPage: 1 } })
        })
        .catch(err => {
          console.log('자유게시판 글작성에 실패하였습니다.')
          console.log(err)
        })
    }
  }
}
</script>
