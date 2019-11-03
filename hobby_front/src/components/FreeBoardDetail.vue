<template>
    <div>
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
                <p>글 내용</p>
                <p>{{post.contents}}</p>
            </div>
            <v-divider class="minDiv mb-5"></v-divider>
            <div class="d-flex justify-end">
                <v-btn
                    dark
                    class="mr-3" 
                    color="light-blue" 
                    >
                    <router-link :to="'/free/' + post.id + '/update'">
                    수정
                    </router-link>
                    </v-btn>
                <v-btn 
                    dark 
                    class="mr-3" 
                    color="pink" 
                    @click="deleteDetail()"
                    >
                    삭제
                </v-btn>
                <v-btn dark to= "/board">
                    목록으로
                </v-btn>
            </div>
        </div>
        <Comment class="mt-10"></Comment>
    </div>
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
    }
    },
    mounted () {
        this.id = this.$route.params.id
        this.getDetail();
    },
    methods: {
        getDetail: function () {
            const baseUrl = this.$store.state.baseUrl
            const apiUrl = baseUrl + 'boards/free/' + this.id 
            this.$http.get(apiUrl)
                .then(res => {
                    this.post = res.data 
                })
                .catch(err => {
                    console.log(err)
                })
        },
        deleteDetail: function () {
            const baseUrl = this.$store.state.baseUrl
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
.minDiv
    border-top-width 2px
</style>