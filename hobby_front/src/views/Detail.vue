<template>
    <div>
        <v-container>
            <v-row>
                <v-col cols="12" md="9">
                    <p>카테고리</p>
                    <h1>글제목</h1>
                    <h3>소제목</h3>
                    <div>
                        <h3>2019-10-30, 8명, 광주 서구</h3>
                    </div>
                </v-col>
                <v-col cols="12" md="3" class="d-flex align-center">
                    <v-btn block dark>참여 신청</v-btn>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols="12" md="7">
                    <v-img src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg" class="mb-12"></v-img>
                    <v-card class="excard">상세모임내용</v-card>
                    <v-card class="excard">모임활동내역</v-card>
                </v-col>
                <v-col cols="12" md="4" offset-md="1">
                    <v-card class="excard">성별, 연령, 비용 등..</v-card>
                    <v-img :src='exImgUrl' class="mb-12"></v-img>
                    <v-card class="excard">
                        <div id="leader">
                            <h3>모임 개설자</h3>
                        </div>
                        <v-divider></v-divider>
                        <div id="member">
                            <h3>참여 멤버 목록</h3>
                        </div>
                    </v-card>
                </v-col>
            </v-row>
        </v-container>
    </div>
</template>

<script>
export default {
    name: 'Detail',
    data() {
        return {
            exImgUrl: 'https://www.google.com/maps/vt/data=STaK-IgFQ8MvHmsBZyhWu0RONtd44KLqPZwgrft2U3OekXRl65Ic0WzehqSi7iRZyjV28YbgetlJUlPJ21uwp4Y7To6K6ZV45tf06YJXxBBBwJBJiQW5Rkv_ebETrk5VeL_3l6W1Ezm5vV3pW2o1yWsSDw-NmFWxtq9DTnglFCmR6zrgpn1AgxPQ9ZPnvrvBdso0-VMrXTFH1WXmH7uxesoYJpy22iLLXR5D'
        }
    }
}
</script>

<style>
.excard {
    height: 300px;
    margin-bottom: 48px;
}
#leader {
    height: 50%;
}
#member {
    height: 50%;
}
</style>