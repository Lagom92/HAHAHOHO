<template>
    <div>
        <v-container>
            <v-row>
                <v-col cols="12" md="6" offset-md="3">
                    <div>
                        <h1>자유게시판 글쓰기</h1>
                    </div>
                    <v-divider></v-divider>
                    <v-form ref="form" v-model="valid">
                        <v-text-field
                        v-model="title"
                        :counter="10"
                        label="글 제목"
                        ></v-text-field>

                        <v-textarea
                        outlined
                        v-model="contents"
                        label="글 내용"
                        ></v-textarea>
                    </v-form>
                </v-col>
            </v-row>
            <v-row>
              <div class="ml-auto">
                <v-btn 
                text color="primary"
                @click="createFree"
                >
                  등록하기
                </v-btn>
              </div>
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
        valid: true,
        }
    },
    
    methods: {
        createFree: function () {
            const baseUrl = this.$store.state.baseUrl
            let form = new FormData()

            form.append('title', this.title)
            form.append('contents', this.contents)
            form.append('user', this.$store.state.user_id)
            form.append('username', this.$store.state.user_name)
            form.append('post', 2) // 2 : 자유 게시판 Default
            const apiUrl = baseUrl + 'boards/free'

            // axios.post(baseUrl + 'boards/free', form, {
            //     headers: {
            //     'Authorization': 'Bearer ' + this.$store.state.user_jwt
            //     }
            // })

            this.$http.post(apiUrl, form)
            .then(res => {
                // window.location.href = 'http://localhost:8080/board';
                // this.$EventBus.$emit('boardPage', 1)
                this.$router.push({path: 'board', porops: {poropsPage: 1}})
                // this.$router.go(-1)
            })
            .catch(err => {
                console.log("자유게시판 글작성에 실패하였습니다.")
                console.log(err)
            })
        },
        
    }
}
</script>