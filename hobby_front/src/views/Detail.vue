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
                    <div class="mb-12" id="mapview">
                        <MapService></MapService>
                    </div>
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
import MapService from '../components/MapService'

export default {
    name: 'Detail',
    components: {
        MapService
    },
    data() {
        return {
            //
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
#mapview {
    height: 300px;
}
</style>