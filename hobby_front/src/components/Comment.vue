<template>
    <div>
        <div>
            <h2 class="my-3">댓글</h2>
        </div>
        <div class="mb-1">
            <v-card>
                <v-container>
                    <p>작성자: {{user}}</p>
                    <v-form>
                        <v-textarea label="댓글 작성"></v-textarea>
                        <div class="d-flex justify-end">
                            <v-btn dark color="light-blue">작성</v-btn>
                        </div>
                    </v-form>
                </v-container>
            </v-card>
        </div>
        <div>
            <v-card>
                <v-container v-for="post in this.posts" :key="post.id">
                    <div>
                        <v-row class="mx-0">
                            <p class="borderP">작성자: {{post.username}}</p>
                            <p>{{post.created_at}}</p>
                        </v-row>
                        <p>{{post.contents}}</p>
                    </div>
                </v-container>
            </v-card>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Comment',
    data () {
        return {
            user: '',
            posts: []
        }

    },
    mounted () {
        this.user = this.$store.state.user_name
        this.id = this.$route.params.id
        this.getComment()
    },
    methods: {
        getComment: function () {
            const baseUrl = this.$store.state.baseUrl
            const apiUrl = baseUrl + 'boards/free/' + this.id + '/comment'
            this.$http.get(apiUrl)
                .then(res => {
                    console.log(res)
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
.borderP
    border-right 1px solid rgba(0, 0, 0, 0.12)
    padding-right 10px
    margin-right 10px
</style>