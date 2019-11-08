<template>
  <v-carousel id="etiquetteCaro" hide-delimiters>
    <v-carousel-item v-for="(slide, i) in slides" :key="i">
      <v-row
      v-if="slide==1"
      id="etiquetteSlide1"
      align="center"
      justify="center"
      >
        <div class="text-center white--text">
          <h1 class="gamjaFont mb-4" id="etiquetteSize">이것만은 꼭!</h1>
          <h4 class="title">
            하하호호는 신뢰있는 서비스를 제공하기 위해 노력하고 있어요.
          </h4>
          <h4 class="title">여러분도 서로를 위해 이것만은 꼭 지켜주세요!</h4>
        </div>
      </v-row>
      <v-row
      v-else-if="slide==2"
      id="etiquetteSlide2"
      align="center"
      justify="center"
      >
        <div>
          <h1 class="gamjaFont mb-10 text-center" id="subTitle">지켜주세요</h1>
          <v-row>
            <v-col cols="12" md="4">
              <v-card  color="#00ff0000" elevation="0">
                <v-icon id="icon" color="black" x-large>
                  mdi-numeric-1-circle
                </v-icon>
                <v-card-title class="headline font-weight-bold" id="textColor">
                  안돼요
                </v-card-title>
                <v-divider class="mx-4"></v-divider>
                <v-card-text class="title" id="textColor">
                  처음 보는 우리<br/>
                  적절한 선을 지켜주세요
                </v-card-text>
              </v-card>
            </v-col>
            <v-col cols="12" md="4">
              <v-card  color="#00ff0000" elevation="0">
                <v-icon id="icon" color="black" x-large>
                  mdi-numeric-2-circle
                </v-icon>
                <v-card-title class="headline font-weight-bold" id="textColor">
                  싫어요
                </v-card-title>
                <v-divider class="mx-4"></v-divider>
                <v-card-text class="title" id="textColor">
                  본인이 신청한 모임에<br/>
                  무단 불참하는 일은 없도록 해요!<br/>
                  약속시간 지키는 것은 필수인거 알죠?
                </v-card-text>
              </v-card>
            </v-col>
            <v-col cols="12" md="4">
              <v-card  color="#00ff0000" elevation="0">
                <v-icon id="icon" color="black" x-large>
                  mdi-numeric-3-circle
                </v-icon>
                <v-card-title class="headline font-weight-bold" id="textColor">
                  하지마세요
                </v-card-title>
                <v-divider class="mx-4"></v-divider>
                <v-card-text class="title" id="textColor">
                  하하호호는<br/>
                  처음 만나는 사람들이 모이는 곳입니다.<br/>
                  함께 즐길 수 있는 모임이 될 수 있도록 서로 배려하는 모습이 필요해요.
                </v-card-text>
              </v-card>
            </v-col>
          </v-row>
        </div>
      </v-row>
    </v-carousel-item>
  </v-carousel>
</template>

<script>
export default {
  data () {
    return {
      slides: [1, 2]
    }
  }
}
</script>

<style lang="stylus">
#etiquetteCaro > div > div > div > div
  height 100% !important

#etiquetteSize
  font-size calc(50px + .8vw)

#textColor
  color black

#icon
  margin-left 10px

#subTitle
  font-size calc(50px + .8vw)
  color black

#etiquetteSlide1
  background-color #ee7789
  height 100% !important

#etiquetteSlide2
  background-color #f1bbba
  height 100% !important
</style>
