<template>
    <div>
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
                <p>글 내용</p>
                <p>{{post.contents}}</p>
            </div>
            <v-divider class="minDiv mb-5"></v-divider>
            <div class="d-flex justify-end">
                <v-btn dark :to="'/board'">목록으로</v-btn>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'NoticeDetail',
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
        const apiUrl = baseUrl + 'boards/notice/' + this.id 
        this.$http.get(apiUrl)
            .then(res => {
                this.post = res.data 
            })
            .catch(err => {
                console.log(err)
            })
        },
    }  
}
</script>

<style lang="stylus">
.minDiv
    border-top-width 2px
</style>