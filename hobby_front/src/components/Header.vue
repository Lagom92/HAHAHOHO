<template>
  <div>
    <v-toolbar fixed>
      <v-container>
        <v-row>
          <v-app-bar-nav-icon id="mobilemenu"></v-app-bar-nav-icon>

          <v-btn text to="/">
            <v-toolbar-title id="title">하하호호</v-toolbar-title>
          </v-btn>

          <v-toolbar-items id="webmenu">
            <v-btn text to="/list">모임</v-btn>
            <v-btn text to="/board">커뮤니티</v-btn>
          </v-toolbar-items>
          <v-spacer></v-spacer>
          <v-toolbar-items>
            <v-btn text @click.stop="dialog = true">
              로그인
            </v-btn>

            <v-dialog v-model="dialog" max-width="280">
              <v-card>
                <v-card-title class="headline">
                  로그인
                  <v-btn class="ml-auto" text @click="dialog = false" >
                    <v-icon>mdi-close</v-icon>
                  </v-btn>
                </v-card-title>
                <v-divider></v-divider>
                <v-card-text class="justify-center">
                  <KakaoLogin></KakaoLogin>
                  <NaverLogin></NaverLogin>
                </v-card-text>
              </v-card>
            </v-dialog>
          </v-toolbar-items>
        </v-row>
      </v-container>
    </v-toolbar>
  </div>
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

<style>
@media screen and (min-width:600px) {
  #mobilemenu {
    display: none;
  }
  #title {
    margin: auto;
    margin-right: 10px;
    margin-left: 10px;
  }
}
@media screen and (max-width:599px) {
  #webmenu {
    display: none;
  }
  #title {
    position: absolute;
    margin: auto;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    text-align: center;
    padding-top: 13px;
  }
}
</style>