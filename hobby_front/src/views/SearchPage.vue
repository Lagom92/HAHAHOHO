<template>
    <div>
        <v-container>
            <SearchBar id="searchPageSearchBar" class="d-flex justify-center my-5"></SearchBar>
            <v-alert border='top' colored-border color="info" elevation="2" class="mt-5 mb-10">
                <p class="mb-0 mt-3">검색키워드 : <strong>{{word}}</strong></p>
            </v-alert>
            <div class="mb-10">
                <v-row class="px-3">
                    <h2>모임 검색결과 ({{cnt}})</h2>
                    <v-spacer></v-spacer>
                    <v-btn text color="#EE7785" @click="$router.push('/list')"><v-icon>mdi-plus</v-icon>더보기</v-btn>
                </v-row>
                <v-divider class="minDiv my-3"></v-divider>
                <v-layout wrap>
                    <v-flex v-for="post in this.posts" v-bind:key="post.id" xs12 sm6 md4>
                        <v-card class="ma-3">
                            <v-img :src="post.photo" height="200px"/>
                            <v-card-title primary-title>
                                <router-link :to="'/list/detail/' + post.id">
                                    <div>
                                        <div class='headline'>{{post.title}}</div>
                                        <span class='grey--text'>{{post.contents}}</span>
                                    </div>
                                </router-link>
                            </v-card-title>
                        </v-card>
                    </v-flex>
                    <!-- 검색 모임이 없는 경우 -->
                    <p v-if="cnt===0">검색 결과가 없습니다.</p>
                </v-layout>
            </div>
            <div class="mb-10">
                <v-row class="px-3">
                    <h2>자유게시판 검색결과 ({{cntF}})</h2>
                    <v-spacer></v-spacer>
                    <v-btn text color="#EE7785" @click="$router.push('/board')"><v-icon>mdi-plus</v-icon>더보기</v-btn>
                </v-row>
                <v-divider class="minDiv my-3"></v-divider>
                <div>
                    <v-row class="font-weight-black my-2">
                        <v-col cols='8'>내용</v-col>
                        <v-col cols='2' class="text-center">작성일시</v-col>
                        <v-col cols='2' class="text-center">작성자</v-col>
                    </v-row>
                    <div v-for="free in frees" v-bind:key="free.id">
                        <router-link :to="'/free/' + free.id">
                            <v-row class="my-2">
                                <v-col cols='8' class="rightBorder">{{free.contents}}</v-col>
                                <v-col cols='2' class="rightBorder text-center">{{free.created_at}}</v-col>
                                <v-col cols='2' class="text-center">{{free.username}}</v-col>
                            </v-row>
                        </router-link>
                        <v-divider></v-divider>
                    </div>
                    <!-- 검색 모임이 없는 경우 -->
                    <p v-if="cntF===0">검색 결과가 없습니다.</p>
                </div>
            </div>
        </v-container>
    </div>
</template>

<script>
import SearchBar from '../components/SearchBar'

export default {
    name: 'SearchPage',
    data() {
        return {
            word: '',
            posts: [],
            cnt: 0,
            frees: [],
            cntF:0
            
        }
    },
    components: {
        SearchBar
    },
    mounted () {
        this.word = this.$store.state.search_word
        this.search()
    },
    methods: {
        search: function () {
        const baseUrl = this.$store.state.baseUrl
        const apiUrl = baseUrl + 'boards/hobby?q=' + this.word
        this.$http.get(apiUrl)
            .then(res => {
            this.cnt = res.data.length
            this.posts = res.data
            })
            .catch(err => {
            console.log(err)
            })

        const api = baseUrl + 'boards/free?q=' + this.word
        this.$http.get(api)
            .then(res => {
            this.cntF = res.data.length
            for (let i of res.data){
                i.created_at = String(i.created_at).substring(0,10)
            }
            this.frees = res.data
            })
            .catch(err => {
            console.log(err)
            })
    }
  }
}
</script>

<style lang="stylus">
.rightBorder
    border-right 1px solid rgba(0, 0, 0, 0.12)

#searchPageSearchBar input
    background #fafafa
</style>