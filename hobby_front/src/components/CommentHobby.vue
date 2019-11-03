<template>
    <div>
        <div>
            <h2 class="my-3">댓글</h2>
        </div>
        <div class="mb-1">
            <v-card>
                <v-container v-if="user !== ''">
                    <p>작성자: {{user}}</p>
                    <v-form>
                        <input v-model="word" label="댓글 작성" placeholder="댓글을 남겨주세요">
                        <div class="d-flex justify-end">
                            <v-btn dark color="light-blue" @click="createComment()">작성</v-btn>
                        </div>
                    </v-form>
                </v-container>
            </v-card>
        </div>
        <div>
            <v-card>
                <v-container v-for="(post, idx) in this.posts" :key="post.id">
                    <div>
                        <v-row class="mx-0">
                            <p><B>{{post.name}}</B></p>
                        </v-row>
                        <p>{{post.contents}}</p>
                        <p>{{post.created_at}}</p>
                        <div class="d-flex justify-end" v-if="userId === post.user">
                            <v-btn dark color="red" @click="deleteComment(post.id, idx)">삭제</v-btn>
                        </div>
                    </div>
                </v-container>
            </v-card>
        </div>
    </div>
</template>

<script>
export default {
    name: 'CommentHobby',
    data () {
        return {
            user: '',
            posts: [],
            word: '',
            userId: ''
        }

    },
    mounted () {
        this.user = this.$store.state.user_name
        this.userId = this.$store.state.user_id
        this.id = this.$route.params.id
        this.getComments()
    },
    methods: {
        getComments () {
            const baseUrl = this.$store.state.baseUrl
            const apiUrl = baseUrl + 'boards/hobby/' + this.id + '/comments'
            this.$http.get(apiUrl)
                .then(res => {
                    for (let i of res.data) {
                        i.created_at = String(i.created_at).substring(0,10)+'  '+String(i.created_at).substring(11,16)
                    }
                    this.posts = res.data 
                })
                .catch(err => {
                    console.log(err)
                })
        },
        createComment () {
            const baseUrl = this.$store.state.baseUrl
            let form = new FormData()

            form.append('name', this.user)
            form.append('user', this.$store.state.user_id)
            form.append('postHobby', this.id)
            form.append('contents', this.word)

            const apiUrl = baseUrl + 'boards/hobby/' + this.id + '/comment'
            this.$http.post(apiUrl, form)
                .then(res => {
                    res.data.created_at = String(res.data.created_at).substring(0,10)+'  '+String(res.data.created_at).substring(11,16)
                    this.posts.unshift(res.data)
                    this.word = ''
                })
                .catch(err => {
                    console.log(err)
                })
        },
        deleteComment (id, idx) {
            const baseUrl = this.$store.state.baseUrl
            const apiUrl = baseUrl + 'boards/hobbyComment/' + id
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

</style>