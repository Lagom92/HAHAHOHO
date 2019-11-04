<template>
  <v-carousel id="introCaro" hide-delimiters style="height:100%">
    <v-carousel-item v-for="(slide, i) in slides" :key="i" style="height:100%">
    <v-parallax v-if="slide==1" src="https://cdn.pixabay.com/photo/2016/04/08/19/51/watercolor-1316867_960_720.jpg" class="pa-10">
        <v-row align="center" justify="center">
            <v-col class="text-center" cols="12"> 
                <h1 class="gamjaFont mb-4" id="introSize">하하호호에서 즐기는 취미생활</h1>
                <h4 class="headline" id="font">하하호호는 공통된 취미를 연결해 모임을 생성해주는 서비스에요.</h4>
                <h4 class="headline" id="font">바쁜 일상에서 벗어나 잊고 있던 취미생활을 즐겨보는 것은 어떨까요?</h4>
            </v-col>
        </v-row>
    </v-parallax>
    <v-parallax v-else-if="slide==2" src="https://cdn.pixabay.com/photo/2019/04/10/11/56/watercolour-4116932_960_720.png" height="900" class="pa-10">
        <v-row align="center" justify="center">
            <v-col cols="12" md="4">
                <v-card  color="#00ff0000" elevation="0">
                    <div class="body-2">비전</div>
                    <v-card-title class="headline font-weight-bold">취미모임생성</v-card-title>
                    <v-divider class="mx-4"></v-divider>
                    <v-card-text class="title">
                        설명
                        <br>설명</v-card-text>
                </v-card>
            </v-col>
            <v-col cols="12" md="4">
                <v-card  color="#00ff0000" elevation="0">
                    <div class="body-2">핵심가치</div>
                    <v-card-title class="headline font-weight-bold">신뢰, 재미, ㅇㅇ</v-card-title>
                    <v-divider class="mx-4"></v-divider>
                    <v-card-text class="title">설명설명</v-card-text>
                </v-card>
            </v-col>
            <v-col cols="12" md="4">
                <v-card  color="#00ff0000" elevation="0">
                    <div class="body-2">미션</div>
                    <v-card-title class="headline font-weight-bold">무슨 사이트</v-card-title>
                    <v-divider class="mx-4"></v-divider>
                    <v-card-text class="title">
                        우리는 ㅇㅇㅇ,ㅇㅇㅇ,ㅇㅇㅇ,ㅇㅇㅇ 4가지의 핵심가치를 가지고 서비스를 제공하고 있어요!
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
    </v-parallax>
    <v-parallax v-else-if="slide==3" src="https://cdn.pixabay.com/photo/2016/04/09/10/26/watercolor-1317812_960_720.jpg"  height="900" class="pa-10">
        <v-row align="center" justify="center">
            <v-col class="text-center" cols="12">
                <h1 class="display-2 font-weight-bold mb-4">하하호호 100% 즐기기</h1>
                <v-row>
                    <v-col cols="12" md="8" offset-md="2">
                        <v-carousel>
                            <v-carousel-item
                            v-for="(item,i) in items"
                            :key="i"
                            :src="item.src"
                            reverse-transition="fade-transition"
                            transition="fade-transition"
                            gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                            >
                                <v-row
                                    class="fill-height"
                                    align="center"
                                    justify="center"
                                >
                                    <div class="display-2 font-weight-bold">{{ item.content }}</div>
                                </v-row>
                            </v-carousel-item>
                        </v-carousel>
                    </v-col>
                </v-row>
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
            slides:[1,2,3],
            items: [
                {
                    src: 'https://cdn.pixabay.com/photo/2016/12/11/18/10/apartment-1899964_960_720.jpg',
                    content: '관심사 찾기'
                },
                {
                    src: 'https://cdn.pixabay.com/photo/2018/03/01/09/33/paper-3190198_960_720.jpg',
                    content: '같이 즐길 모임 찾기',
                },
                {
                    src: 'https://cdn.pixabay.com/photo/2019/10/21/10/34/meeting-4565703_960_720.jpg',
                    content: '마음껏 즐기기',
                },
            ],
        }
    }
}
</script>

<style>
#introCaro > div > div > div > div {
    height: 100% !important;
}
#introCaro > div > div > div > div > div > div {
    height: 100% !important;
}
#introSize {
    font-size: 100px;
    color: black;
}
#font {
    color: black;
}
</style>
