<template>
    <div>
        <div>
            <h2 class="my-3">댓글</h2>
        </div>
        <div class="mb-1">
            <v-card>
                <v-container>
                    <p>작성자</p>
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
                <v-container>
                    <div>
                        <v-row class="mx-0">
                            <p class="borderP">작성자</p>
                            <p>2019-10-31</p>
                        </v-row>
                        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
                    </div>
                </v-container>
            </v-card>
            <v-card>
                <v-container>
                    <div>
                        <v-row class="mx-0">
                            <p class="borderP">작성자</p>
                            <p>2019-10-31</p>
                        </v-row>
                        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
                    </div>
                </v-container>
            </v-card>
            <v-card>
                <v-container>
                    <div>
                        <v-row class="mx-0">
                            <p class="borderP">작성자</p>
                            <p>2019-10-31</p>
                        </v-row>
                        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
                        <v-divider class="mb-3"></v-divider>
                        <div class="d-flex justify-end">
                            <v-btn dark color="light-blue" class="mr-3">수정</v-btn>
                            <v-btn dark color="pink">삭제</v-btn>
                        </div>
                    </div>
                </v-container>
            </v-card>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Comment'
}
</script>

<style lang="stylus">
.borderP
    border-right 1px solid rgba(0, 0, 0, 0.12)
    padding-right 10px
    margin-right 10px
</style>