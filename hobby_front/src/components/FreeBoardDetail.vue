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
                <p>{{post.contents}}</p>
            </div>
            <v-divider class="minDiv mb-5"></v-divider>
            <div class="d-flex justify-end">
                <v-btn
                    dark
                    class="mr-3" 
                    color="light-blue"
                    v-if="user === post.user"
                    @click="$router.push({ name: 'updatefreeboard', params: { id: post.id }})"
                    >
                    수정
                    </v-btn>
                <v-btn 
                    dark 
                    class="mr-3" 
                    color="pink" 
                    @click="deleteDetail()"
                    v-if="user === post.user"
                    >
                    삭제
                </v-btn>
                <v-btn dark to= "/board" color="#74B4A0">
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
        this.getDetail();
    },
    methods: {
        getDetail: function () {
            const baseUrl = this.$store.state.baseUrl
            const apiUrl = baseUrl + 'boards/free/' + this.id 
            this.$http.get(apiUrl)
                .then(res => {
                    let created_at = res.data.created_at
                    res.data.created_at = created_at.substring(0,4)+'년 '+created_at.substring(5,7)+'월 '+created_at.substring(8,10)+'일' 

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