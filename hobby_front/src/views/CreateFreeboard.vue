<template>
    <div>
        <v-container>
            <v-row>
                <v-col cols="12" md="6" offset-md="3">
                    <div>
                        <h1>자유게시판 글쓰기</h1>
                    </div>
                    <v-divider></v-divider>
                    <v-form ref="form" v-model="valid">
                        <v-text-field
                        v-model="title"
                        :counter="10"
                        label="글 제목"
                        ></v-text-field>

                        <v-textarea
                        outlined
                        v-model="contents"
                        label="글 내용"
                        ></v-textarea>
                    </v-form>
                </v-col>
            </v-row>
            <v-row>
              <div class="ml-auto">
                <v-btn text color="primary">
                  등록하기
                </v-btn>
              </div>
            </v-row>
        </v-container>
    </div>
</template>

<script>
export default {
    name: 'CreateFreeboard',
    data () {
        return {
        title: '',
        content: '',
        valid: true,
        }
    }
}
</script>