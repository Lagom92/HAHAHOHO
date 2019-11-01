<template>
    <div>
        <v-container>
            <SearchBar class="d-flex justify-center my-5"></SearchBar>
            <v-alert border='top' colored-border color="info" elevation="2" class="mt-5 mb-10">
                <p class="mb-0 mt-3">검색키워드 : <strong>ㅇㅇㅇ</strong></p>
            </v-alert>
            <div class="mb-10">
                <v-row class="px-3">
                    <h2>모임 검색결과 (10)</h2>
                    <v-spacer></v-spacer>
                    <v-btn text color="#EE7785" @click="$router.push('/list')"><v-icon>mdi-plus</v-icon>더보기</v-btn>
                </v-row>
                <v-divider class="minDiv my-3"></v-divider>
                <v-layout wrap>
                    <v-flex v-for="i in this.limits" v-bind:key="i" xs12 sm6 md4>
                        <v-card class="ma-3">
                            <v-img src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg" height="200px"/>
                            <v-card-title primary-title>
                                <div>
                                    <div class='headline'>title</div>
                                    <span class='grey--text'>body</span>
                                </div>
                            </v-card-title>
                        </v-card>
                    </v-flex>
                </v-layout>
            </div>
            <div class="mb-10">
                <v-row class="px-3">
                    <h2>자유게시판 검색결과 (22)</h2>
                    <v-spacer></v-spacer>
                    <v-btn text color="#EE7785" @click="$router.push('/board')"><v-icon>mdi-plus</v-icon>더보기</v-btn>
                </v-row>
                <v-divider class="minDiv my-3"></v-divider>
                <div>
                    <div v-for="i in this.limits" v-bind:key="i">
                        <v-row class="my-2">
                            <v-col cols='8' class="rightBorder">자유게시판 글</v-col>
                            <v-col cols='2' class="rightBorder text-center">2019-11-01</v-col>
                            <v-col cols='2' class="text-center">작성자</v-col>
                        </v-row>
                        <v-divider></v-divider>
                    </div>
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
            limits: 3
        }
    },
    components: {
        SearchBar
    }
}
</script>

<style lang="stylus">
.rightBorder
    border-right 1px solid rgba(0, 0, 0, 0.12)
</style>