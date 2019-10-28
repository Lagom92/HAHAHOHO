<template>
    <div>
        <v-container>
            <v-row>
                <v-col cols="12" md="5">
                    <v-chip small color="#9AB878" dark>국내여행</v-chip>
                    <h1>할로윈 파티 하실 분 모집</h1>
                </v-col>
                <v-col cols="12" md="2">
                    <v-menu
                        transition="scale-transition"
                    >
                        <template v-slot:activator="{ on }">
                            <v-chip pill v-on="on" class="mt-8">
                                <v-avatar left>
                                <v-img src="https://cdn.vuetifyjs.com/images/john.png"></v-img>
                                </v-avatar>
                                작성자
                            </v-chip>
                        </template>
                        <v-card width="300">
                            <v-list dark>
                                <v-list-item>
                                    <v-list-item-avatar>
                                        <v-img src="https://cdn.vuetifyjs.com/images/john.png"></v-img>
                                    </v-list-item-avatar>
                                    <v-list-item-content>
                                        <v-list-item-title>작성자</v-list-item-title>
                                        <v-list-item-subtitle>친절함 활발함</v-list-item-subtitle>
                                    </v-list-item-content>
                                    <v-list-item-action>
                                        <v-btn icon >
                                            <v-icon>mdi-chevron-right</v-icon>
                                        </v-btn>
                                    </v-list-item-action>
                                </v-list-item>
                            </v-list>
                        </v-card>
                    </v-menu>
                </v-col>
                <v-col cols="12" md="4" offset-md="1" class="d-flex align-center" >
                    <v-btn block dark color="#F3B749">참여하기</v-btn>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols="12" md="7">
                    <v-img src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg" class="mb-12"></v-img>
                    <v-card class="excard">
                        <v-card-title class="mb-3">
                            모임 소개
                        </v-card-title>
                        <v-card-text class="text--primary">
                            <div>
                                할로윈파티 하고 싶은데 못하시는 분!!
                                <br>같이 놀아요~~
                            </div>
                        </v-card-text>
                    </v-card>
                </v-col>
                <v-col cols="12" md="4" offset-md="1">
                    <v-card class="excard">
                        <v-card-title class="mb-3">
                            모임 정보
                        </v-card-title>
                        <v-card-text class="text--primary">
                            <div class="mb-4">
                                <v-icon class="mr-1">mdi-calendar-month</v-icon> 2019년 10월 31일 목요일
                            </div>
                            <div class="mb-4">
                                <v-icon class="mr-1">mdi-clock-outline</v-icon> 오후 6시
                            </div>
                            <div class="mb-4">
                                <v-icon class="mr-1">mdi-map-marker</v-icon> 광주 서구 스타벅스 앞
                            </div>
                            <div class="mb-4">
                                <v-icon class="mr-1">mdi-account</v-icon> 10명 (20-30대)
                            </div>
                            <div class="mb-4">
                                <v-icon class="mr-1">mdi-gender-male-female</v-icon> 상관없음
                            </div>
                            <div class="mb-4">
                                <v-icon class="mr-1">mdi-currency-krw</v-icon> 10,000원
                            </div>
                        </v-card-text>
                    </v-card>
                    <div class="mb-12" id="mapview">
                        <MapService></MapService>
                    </div>
                    <v-card class="excard">
                        <div id="member">
                            <v-card-title class="mb-3">
                                모임 멤버 (1 / 10)
                            </v-card-title>
                            <v-chip pill class="ma-3">
                                <v-avatar left>
                                <v-img src="https://cdn.vuetifyjs.com/images/john.png"></v-img>
                                </v-avatar>
                                작성자
                            </v-chip>
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