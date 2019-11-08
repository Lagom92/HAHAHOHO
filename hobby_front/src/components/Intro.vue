<template>
  <v-carousel id="introCaro" hide-delimiters>
    <v-carousel-item v-for="(slide, i) in slides" :key="i">
      <v-row v-if="slide==1" id="introSlide1" justify="center" align="center">
        <div class="text-center white--text">
          <h1 class="gamjaFont mb-4" id="introSize">
            하하호호에서 즐기는 취미생활
          </h1>
          <h4 class="title">
            하하호호는 공통된 취미를 연결해 모임을 생성해주는 서비스에요.
          </h4>
          <h4 class="title">
            바쁜 일상에서 벗어나 잊고 있던 취미생활을 즐겨보는 것은 어떨까요?
          </h4>
        </div>
      </v-row>
      <v-row
      v-else-if="slide==2"
      id="introSlide2"
      justify="center"
      align="center"
      >
        <div>
          <h1 class="gamjaFont mb-10 text-center" id="subTitle">
            우리 사이트는요
          </h1>
          <v-row>
            <v-col class="px-10" cols="12" md="4">
              <v-card color="#00ff0000" elevation="0">
                <v-icon class="mb-5" id="icon" color="black" x-large>
                  mdi-numeric-1-circle
                </v-icon>
                <v-img
                src="../assets/business.png"
                class="d-none d-md-flex"
                height="200"
                width="200"
                ></v-img>
                <v-card-title class="headline font-weight-bold" id="textColor">
                  함께 만나요
                </v-card-title>
              </v-card>
            </v-col>
            <v-col class="px-10" cols="12" md="4">
              <v-card color="#00ff0000" elevation="0">
                <v-icon class="mb-5" id="icon" color="black" x-large>
                  mdi-numeric-2-circle
                </v-icon>
                <v-img
                src="../assets/pinky-promise.png"
                class="d-none d-md-flex"
                height="200"
                width="200"
                ></v-img>
                <v-card-title class="headline font-weight-bold" id="textColor">
                  신뢰
                </v-card-title>
              </v-card>
            </v-col>
            <v-col cols="12" md="4" class="px-10">
              <v-card color="#00ff0000" elevation="0">
                <v-icon class="mb-5" id="icon" color="black" x-large>
                  mdi-numeric-3-circle
                </v-icon>
                <v-img
                src="../assets/laugh.png"
                class="d-none d-md-flex"
                height="200"
                width="200"
                ></v-img>
                <v-card-title class="headline font-weight-bold" id="textColor">
                  즐거움
                </v-card-title>
              </v-card>
            </v-col>
          </v-row>
        </div>
      </v-row>
      <div v-else-if="slide==3" id="introSlide3">
        <v-row align="center" justify="center">
          <v-col class="text-center" cols="12">
            <h1 class="gamjaFont mt-10 mb-5" id="subTitle">
              하하호호 100% 즐기기
            </h1>
            <v-row>
              <v-col cols="12" md="8" offset-md="2">
                <v-carousel
                :show-arrows="false"
                height="400"
                delimiter-icon="mdi-minus"
                hide-delimiter-background
                >
                  <v-carousel-item
                  v-for="(item,j) in items"
                  :key="j"
                  :src="item.src"
                  gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                  >
                    <v-row
                    class="fill-height"
                    align="center"
                    justify="center"
                    >
                      <div class="display-2 font-weight-bold white--text">
                        {{ item.content }}
                      </div>
                    </v-row>
                  </v-carousel-item>
                </v-carousel>
              </v-col>
            </v-row>
          </v-col>
        </v-row>
      </div>
    </v-carousel-item>
  </v-carousel>
</template>

<script>
export default {
  data () {
    return {
      slides: [1, 2, 3],
      items: [
        {
          src: 'https://cdn.pixabay.com/photo/2016/12/11/18/10/apartment-1899964_960_720.jpg',
          content: '관심사 찾기'
        },
        {
          src: 'https://cdn.pixabay.com/photo/2018/03/01/09/33/paper-3190198_960_720.jpg',
          content: '같이 즐길 모임 찾기'
        },
        {
          src: 'https://cdn.pixabay.com/photo/2019/10/21/10/34/meeting-4565703_960_720.jpg',
          content: '마음껏 즐기기'
        }
      ]
    }
  }
}
</script>

<style lang="stylus">
#introCaro > div > div > div > div
  height 100% !important

#introSize
  font-size calc(50px + .8vw)

#textColor
  color black

#subTitle
  font-size calc(4px + .8vw)
  color black

#icon
  margin-left 10px

#introSlide1
  background-color #3E9278
  height 100% !important

#introSlide2
  background-color #74BAA0
  height 100% !important

#introSlide3
  background-color #b8d8c0
  height 100% !important
</style>
