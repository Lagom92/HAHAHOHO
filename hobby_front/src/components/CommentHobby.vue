<template>
    <div>
        <div class="mb-1">
            <v-card color="#fafafa" flat>
                <v-container v-if="user !== ''">
                    <v-row align="center" class="createuser px-3">
                        <div>작성자 : <span class="font-weight-black">{{user}}</span></div>
                        <v-spacer></v-spacer>
                        <v-btn color="primary" text icon @click="createComment()">
                            <v-icon>mdi-pencil</v-icon>
                        </v-btn>
                    </v-row>
                    <v-text-field
                        v-model="word"
                        label="댓글 작성"
                        placeholder="주제와 무관한 댓글, 타인의 권리를 침해하거나 명예를 훼손하는 댓글은 별도의 통보 없이 재제를 받을 수 있습니다."
                        outlined
                        shaped
                        @keyup.enter="createComment()"
                    ></v-text-field>
                </v-container>
            </v-card>
        </div>
        <div>
            <v-card color="#fafafa" flat v-for="(post, idx) in this.posts" :key="post.id">
                <v-container>
                    <div>
                        <v-row class="mx-0">
                            <v-row align="center" class="createuser px-3">
                                <div class="font-weight-black">{{post.name}}</div>
                                <v-divider vertical inset class="mx-5"></v-divider>
                                <div>{{post.created_at}}</div>
                                <v-spacer></v-spacer>
                                <v-btn v-if="userId === post.user" text icon @click="deleteComment(post.id, idx)">
                                    <v-icon color="error">mdi-trash-can-outline</v-icon>
                                </v-btn>
                            </v-row>
                        </v-row>
                        <p class="mb-0">{{post.contents}}</p>
                    </div>
                </v-container>
                <v-divider></v-divider>
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

.createuser
    height 45px
</style>