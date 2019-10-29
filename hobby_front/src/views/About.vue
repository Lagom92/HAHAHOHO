<template>
    <div>
        <v-tabs v-model="tabs" centered>
            <v-tab>소개</v-tab>
            <v-tab>에티켓</v-tab>
            <v-tab>운영방침</v-tab>
        </v-tabs>
        <v-tabs-items v-model="tabs">
            <v-tab-item>
                <v-parallax src="https://cdn.vuetifyjs.com/images/parallax/material.jpg">
                    <v-row align="center" justify="center">
                        <v-col class="text-center" cols="12">
                            <h1 class="display-1 font-weight-thin mb-4">우리는 하하호호 입니다.</h1>
                            <h4 class="subheading">취미가 같은 여러분들의 모임을 쉽게 도와줄거에요!</h4>
                        </v-col>
                    </v-row>
                </v-parallax>
                <v-parallax src="https://cdn.vuetifyjs.com/images/parallax/material2.jpg">
                    <v-row align="center" justify="center">
                        <v-card raised>
                            <v-card-title>우리는 하하호호 입니다.</v-card-title>
                            <v-divider class="mx-4"></v-divider>
                            <v-card-text>우리는 취미가 같은 여러분들이 쉽게 모일 수 있도록 도와줄거에요!</v-card-text>
                        </v-card>
                    </v-row>
                </v-parallax>
            </v-tab-item>
            <v-tab-item>
                <v-parallax src="https://cdn.vuetifyjs.com/images/parallax/material2.jpg">
                    <v-row align="center" justify="center">
                        <v-col class="text-center" cols="12">
                            <h1 class="display-1 font-weight-thin mb-4">하하호호 에티켓입니다.</h1>
                            <h4 class="subheading">모임에서 말없이 불참하는 행동 하지 말아요!</h4>
                        </v-col>
                    </v-row>
                </v-parallax>
                <v-parallax src="https://cdn.vuetifyjs.com/images/backgrounds/vbanner.jpg">
                    <v-row align="center" justify="center">
                        <v-card raised>
                            <v-card-title>하하호호 에티켓입니다.</v-card-title>
                            <v-divider class="mx-4"></v-divider>
                            <v-card-text>모임에서 말없이 불참하는 행동 하지 말아요!</v-card-text>
                        </v-card>
                    </v-row>
                </v-parallax>
            </v-tab-item>
            <v-tab-item>
                <v-parallax src="https://cdn.vuetifyjs.com/images/backgrounds/vbanner.jpg">
                    <v-row align="center" justify="center">
                        <v-col class="text-center" cols="12">
                            <h1 class="display-1 font-weight-thin mb-4">하하호호 운영방침입니다.</h1>
                            <h4 class="subheading">자꾸 모임에 불참하면 서비스 이용을 못하게 할거에요!</h4>
                        </v-col>
                    </v-row>
                </v-parallax>
                <v-parallax src="https://cdn.vuetifyjs.com/images/parallax/material.jpg">
                    <v-row align="center" justify="center">
                        <v-card raised>
                            <v-card-title>하하호호 운영방침입니다.</v-card-title>
                            <v-divider class="mx-4"></v-divider>
                            <v-card-text>자꾸 모임에 불참하면 서비스 이용을 못하게 할거에요!</v-card-text>
                        </v-card>
                    </v-row>
                </v-parallax>
            </v-tab-item>
        </v-tabs-items>
    </div>
</template>

<script>
export default {
    name: 'About',
    data() {
        return {
            tabs: null
        }
    }
}
</script>

<style lang="stylus">

</style>