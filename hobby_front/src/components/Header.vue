<template>
  <v-app-bar app elevate-on-scroll>
    <v-container>
      <v-toolbar flat>
        <v-btn text>
          <v-toolbar-title>하하호호</v-toolbar-title>
        </v-btn>
        <v-toolbar-items>
          <v-btn text @click="$router.push('/list')">모임</v-btn>
          <v-btn text @click="$router.push('/board')">커뮤니티</v-btn>
        </v-toolbar-items>
        <v-spacer></v-spacer>
        <v-toolbar-items>
          <v-btn text @click.stop="dialog = true">로그인</v-btn>
          <v-dialog v-model="dialog">
            <v-card>
              <v-card-title>로그인</v-card-title>
              <v-card-text>
                <KakaoLogin></KakaoLogin>
                <NaverLogin></NaverLogin>
              </v-card-text>
            </v-card>
          </v-dialog>
        </v-toolbar-items>
      </v-toolbar>
    </v-container>
  </v-app-bar>
</template>

<script>
import KakaoLogin from '@/components/KakaoLogin'
import NaverLogin from '@/components/NaverLogin'

export default {
  name: 'Header',
  components: {
    KakaoLogin,
    NaverLogin,
  },
  data () {
    return {
      dialog: false,
    }
  },
}
</script>

<style lang="stylus">

</style>