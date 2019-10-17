<template>
    <div>
        <v-container>
            <v-row>
                <v-col cols="9">
                    <p>카테고리</p>
                    <h1>글제목</h1>
                    <h3>소제목</h3>
                    <div>
                        <h3>2019-10-30, 8명, 광주 서구</h3>
                    </div>
                </v-col>
                <v-col cols="3">
                    <button>참여 신청</button>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols="7">
                    <v-card class="excard">사진</v-card>
                    <v-card class="excard">상세내용</v-card>
                    <v-card class="excard">활동내용</v-card>
                </v-col>
                <v-col cols="4" offset="1">
                    <v-card class="excard">성별, 연령, 상세위치, 비용 등..</v-card>
                    <v-card class="excard">참여멤버 목록</v-card>
                    <v-card class="excard">지도</v-card>
                </v-col>
            </v-row>
        </v-container>
    </div>
</template>

<script>
export default {
    name: 'Detail'
}
</script>

<style>
.excard {
    height: 300px;
    margin-bottom: 50px;
}
</style>