<template>
  <div>
    <v-app-bar app elevate-on-scroll>
      <v-container>
        <v-toolbar flat>
          <v-app-bar-nav-icon class="d-sm-none d-flex" @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
          <v-spacer class="d-sm-none d-flex"></v-spacer>
          <v-toolbar-title class="gamjaFont px-4" @click="$router.push('/')" id="hahahoho">
            하하호호
          </v-toolbar-title>
          <v-toolbar-items class="d-sm-flex d-none">
            <v-btn text @click="$router.push('/about')" class="nanumFont">소개</v-btn>
            <v-btn text @click="$router.push('/list')" class="nanumFont">모임</v-btn>
            <v-btn text @click="$router.push('/board')" class="nanumFont">커뮤니티</v-btn>
          </v-toolbar-items>
          <v-spacer></v-spacer>
          <v-btn v-if="state" icon class="d-sm-none d-flex" @click.stop="dialog = true">
            <v-icon>mdi-account</v-icon>
          </v-btn>
          <v-btn v-else icon class="d-sm-none d-flex" @click="$router.push('/user')">
            <v-icon>mdi-account</v-icon>
          </v-btn>
          <v-toolbar-items class="d-sm-flex d-none align-center">
            <v-btn v-if="state" text @click.stop="dialog = true" class="nanumFont">로그인</v-btn>
            <v-row v-else>
              <div class="my-auto">
                <p class="mb-0 mr-5">{{username}}님 환영합니다</p>
              </div>
              <v-btn text @click.stop="logout()" class="nanumFont">로그아웃</v-btn>
            </v-row>
            <v-dialog v-model="dialog" width="330">
              <v-card class="text-center">
                <v-card-title class="nanumFont">로그인</v-card-title>
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
      <v-list-item v-if="state">
        <v-list-item-content>
          <v-btn dark color="#3e9278" @click.stop="dialog = true" class="nanumFont">로그인</v-btn>
        </v-list-item-content>
      </v-list-item>
      <v-list-item v-else>
        <v-list-item-avatar>
          <v-img src="https://randomuser.me/api/portraits/men/78.jpg"></v-img>
        </v-list-item-avatar>
        <v-list-item-content>
          <v-list-item-title class="title nanumFont">
            {{username}}
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>
      <v-list nav dense>
        <v-list-item-group v-model="group">
          <v-list-item v-for="item in items" :key="item.path" :to="{ path : item.path }">
            <v-list-item-icon>
              <v-icon color="#EE7785">mdi-water</v-icon>
            </v-list-item-icon>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>

      <template v-if="state==false" v-slot:append>
        <div class="pa-2">
          <v-btn block dark @click.stop="logout()" color="#3e9278" class="nanumFont">로그아웃</v-btn>
        </div>
      </template>
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
      username: '',
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
      this.username = this.$store.state.user_name
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

<style lang="stylus">
.nanumFont
  font-family 'Nanum Gothic', sans-serif

#hahahoho
 color #EE7785
</style>