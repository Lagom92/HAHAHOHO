<template>
    <div>
        <section id='top'>
            <h1 class="mb-3">자유게시판</h1>
            <v-divider id='topdivider'></v-divider>
            <v-row class="font-weight-black">
                <v-col cols='8'>내용</v-col>
                <v-col cols='2'>작성일시</v-col>
                <v-col cols='2'>작성자</v-col>
            </v-row>
        </section>
        <v-divider class='middivider'></v-divider>
        <section id='content'>
            <div v-for="i in 10" v-bind:key="i">
                <a href="#">
                    <v-row>
                        <v-col cols='8'>자유게시판 내용</v-col>
                        <v-col cols='2'>2019-10-16</v-col>
                        <v-col cols='2'>테스트유저</v-col>
                    </v-row>
                </a>
                <v-divider class='middivider' v-if="i % 3 == 0"></v-divider>
                <v-divider v-else></v-divider>
            </div>
        </section>
    </div>
</template>

<script>
export default {
    name: 'FreeBoard'
}
</script>

<style>
#topdivider {
    border-top-width: 2px;
    border-top-color: #000;
}
.middivider {
    border-top-width: 2px;
}
</style>