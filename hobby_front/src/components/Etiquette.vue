<template>
  <v-carousel id="etiquetteCaro" hide-delimiters>
    <v-carousel-item v-for="(slide, i) in slides" :key="i">
        <v-parallax v-if="slide==1" src="https://www.colorbook.io/imagecreator.php?hex=ee7789&width=1920&height=1080&text=%201920x1080" class="pa-10">
            <v-row align="center" justify="center">
                <v-col class="text-center" cols="12">
                    <h1 class="gamjaFont mb-4" id="etiquetteSize">이것만은 꼭! </h1>
                    <h4 class="headline">하하호호는 신뢰있는 서비스를 제공하기 위해 노력하고 있어요.</h4>
                    <h4 class="headline">여러분도 서로를 위해 이것만은 꼭 지켜주세요!</h4>
                </v-col>
            </v-row>
        </v-parallax>
        <v-parallax v-else-if="slide==2" src="https://cdn.pixabay.com/photo/2019/04/10/11/56/watercolour-4116932_960_720.png" height="900" class="pa-10">
            <v-row align="center" justify="center">
                <v-col cols="12" md="4">
                    <v-card  color="#00ff0000" elevation="0">
                        <v-icon x-large>mdi-numeric-1-circle</v-icon>
                        <v-card-title class="headline font-weight-bold">하하호호</v-card-title>
                        <v-divider class="mx-4"></v-divider>
                        <v-card-text class="title">
                            룰루루랄랄라
                            <br>하하호호 웃음보터지는 모임을 만들어요~
                        </v-card-text>
                    </v-card>
                </v-col>
                <v-col cols="12" md="4">
                    <v-card  color="#00ff0000" elevation="0">
                        <v-icon x-large>mdi-numeric-2-circle</v-icon>
                        <v-card-title class="headline font-weight-bold">책임감</v-card-title>
                        <v-divider class="mx-4"></v-divider>
                        <v-card-text class="title">
                            본인이 신청한 모임에 무단 불참하는 일은 없도록 해요!
                            <br>약속시간 지키는 것은 필수인거 알죠?
                        </v-card-text>
                    </v-card>
                </v-col>
                <v-col cols="12" md="4">
                    <v-card  color="#00ff0000" elevation="0">
                        <v-icon x-large>mdi-numeric-3-circle</v-icon>
                        <v-card-title class="headline font-weight-bold">배려</v-card-title>
                        <v-divider class="mx-4"></v-divider>
                        <v-card-text class="title">
                            하하호호는 처음 만나는 사람들이 모이는 곳입니다.
                            <br>함께 즐길 수 있는 모임이 될 수 있도록 서로 배려하는 모습이 필요해요.
                        </v-card-text>
                    </v-card>
                </v-col>
            </v-row>
        </v-parallax>
    </v-carousel-item>
  </v-carousel>
</template>

<script>
export default {
    data() {
        return {
            slides: [1,2],
        }
    }
}
</script>

<style>
#etiquetteCaro > div > div > div > div {
    height: 100% !important
}
#etiquetteCaro > div > div > div > div > div > div {
    height: 100% !important
}
#etiquetteSize{
    font-size: 100px;
}
</style>
