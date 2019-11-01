<template>
  <div>
    <v-app-bar app elevate-on-scroll>
      <v-container>
        <v-toolbar flat>
          <v-app-bar-nav-icon class="d-sm-none d-flex" @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
          <v-spacer class="d-sm-none d-flex"></v-spacer>
          <v-toolbar-title class="px-4" @click="$router.push('/')">하하호호</v-toolbar-title>
          <v-toolbar-items class="d-sm-flex d-none">
            <v-btn text @click="$router.push('/about')">소개</v-btn>
            <v-btn text @click="$router.push('/list')">모임</v-btn>
            <v-btn text @click="$router.push('/board')">커뮤니티</v-btn>
          </v-toolbar-items>
          <v-spacer></v-spacer>
          <v-btn icon class="d-sm-none d-flex" @click.stop="dialog = true">
            <v-icon>mdi-account</v-icon>
          </v-btn>
          <v-toolbar-items class="d-sm-flex d-none">
            <v-btn v-if="state" text @click.stop="dialog = true">로그인</v-btn>
            <v-btn v-else text @click.stop="logout()">로그아웃</v-btn>
            <v-dialog v-model="dialog" width="330">
              <v-card class="text-center">
                <v-card-title>로그인</v-card-title>
                <v-divider class="mx-5 mb-5"></v-divider>
                <v-card-text>
                  <KakaoLogin class="mb-2"></KakaoLogin>
                  <NaverLogin></NaverLogin>
                </v-card-text>
              </v-card>
            </v-dialog>
          </v-toolbar-items>
        </v-toolbar>
      </v-container>
    </v-app-bar>
    <v-navigation-drawer v-model="drawer" fixed temporary class="d-sm-none d-flex">
      <v-list nav dense>
        <v-list-item-group v-model="group">
          <v-list-item v-for="item in items" :key="item.path" :to="{ path : item.path }">
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
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
      drawer: false,
      group: null,
      state: true,
      items: [
        { title: '소개', path: 'about' },
        { title: '모임', path: 'list' },
        { title: '커뮤니티', path: 'board' }
      ]
    }
  },
  watch: {
    group() {
      this.drawer = false
    },
  },
  mounted() {
    if(this.$store.state.user_jwt){
      this.state = false
    }
  },
  methods: {
    logout() {
      let scope = this
      Kakao.Auth.logout(function (){
        scope.$store.commit('jwtSave', '')
        scope.$store.commit('idSave', '')
        scope.$store.commit('nameSave', '')
        Kakao.cleanup()
        location.reload()
        location.href('http://localhost:8080/')
        scope.state = true
      })
    }
  }
}
</script>
