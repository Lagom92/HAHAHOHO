<template>
    <div>
        <div>
            <h1 class="my-3">로렘 입숨</h1>
            <v-row class="px-3">
                <p class="borderP">2019-10-30</p>
                <p>작성자</p>
                <v-spacer></v-spacer>
                <p class="borderP">조회수: 0</p>
                <p>댓글수: 0</p>
            </v-row>
        </div>
        <v-divider class="minDiv mb-5"></v-divider>
        <div>
            <div>
                <p>글 내용</p>
                <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
                <p>글 내용</p>
                <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
            </div>
            <v-divider class="minDiv mb-5"></v-divider>
            <div class="d-flex justify-end">
                <v-btn dark class="mr-3" color="light-blue">
                    수정
                </v-btn>
                <v-btn dark class="mr-3" color="pink">
                    삭제
                </v-btn>
                <v-btn dark>
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
    }
}
</script>

<style lang="stylus">
.minDiv
    border-top-width 2px
</style>