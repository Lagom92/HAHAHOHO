<template>
  <div>
    <v-app-bar app elevate-on-scroll>
      <v-container>
        <v-toolbar flat>
          <v-app-bar-nav-icon
          @click.stop="drawer = !drawer"
          class="d-sm-none d-flex"
          ></v-app-bar-nav-icon>
          <v-spacer class="d-sm-none d-flex"></v-spacer>
          <v-avatar class="d-none d-sm-flex" size="48">
            <img
            src="../assets/hahoicon.png"
            @click="$router.push('/').catch(err => {})"
            id="logo"
            >
          </v-avatar>
          <v-toolbar-title
          @click="$router.push('/').catch(err => {})"
          class="gamjaFont px-4"
          id="hahahoho"
          >
            하하호호
          </v-toolbar-title>
          <v-toolbar-items class="d-sm-flex d-none">
            <v-btn
            @click="$router.push('/about').catch(err => {})"
            class="nanumFont"
            text
            >
              소개
            </v-btn>
            <v-btn
            @click="$router.push('/list').catch(err => {})"
            class="nanumFont"
            text
            >
              모임
            </v-btn>
            <v-btn
            @click="$router.push('/board').catch(err => {})"
            class="nanumFont"
            text
            >
              커뮤니티
            </v-btn>
          </v-toolbar-items>
          <v-spacer></v-spacer>
          <v-btn
          v-if="state"
          @click.stop="dialog = true"
          class="d-sm-none d-flex"
          icon
          >
            <v-icon>mdi-account</v-icon>
          </v-btn>
          <v-btn
          v-else
          @click="$router.push('/user').catch(err => {})"
          class="d-sm-none d-flex"
          icon
          >
            <v-icon>mdi-account</v-icon>
          </v-btn>
          <v-toolbar-items class="d-sm-flex d-none align-center">
            <v-btn
            v-if="state"
            @click.stop="dialog = true"
            class="nanumFont"
            text
            >
              로그인
            </v-btn>
            <v-row v-else>
              <div class="my-auto">
                <p
                @click="$router.push('/user').catch(err => {})"
                class="mb-0 mr-5"
                id="userrouter"
                >
                  {{username}}님 환영합니다
                </p>
              </div>
              <v-btn @click.stop="logout()" class="nanumFont" text>
                로그아웃
              </v-btn>
            </v-row>
            <v-dialog v-model="dialog" width="330">
              <v-card class="text-center">
                <v-card-title class="nanumFont">로그인</v-card-title>
                <v-divider class="mx-5 mb-5"></v-divider>
                <v-card-text>
                  <KakaoLogin class="mb-2"></KakaoLogin>
                  <img
                  src="../assets/naver.png"
                  @click="stop()"
                  width="222"
                  height="49"
                  >
                </v-card-text>
              </v-card>
            </v-dialog>
          </v-toolbar-items>
        </v-toolbar>
      </v-container>
    </v-app-bar>
    <v-navigation-drawer
    v-model="drawer"
    class="d-sm-none d-flex"
    fixed
    temporary
    >
      <v-list-item v-if="state">
        <v-list-item-content>
          <v-btn
          @click.stop="dialog = true"
          class="nanumFont"
          color="#3e9278"
          dark
          >
            로그인
          </v-btn>
        </v-list-item-content>
      </v-list-item>
      <v-list-item v-else>
        <v-list-item-avatar>
          <v-img :src="img"></v-img>
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
          <v-list-item
          v-for="item in items"
          :key="item.path"
          :to="{ path : item.path }"
          >
            <v-list-item-icon>
              <v-icon color="#EE7785">mdi-water</v-icon>
            </v-list-item-icon>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>

      <template v-if="state==false" v-slot:append>
        <div class="pa-2">
          <v-btn
          @click.stop="logout()"
          class="nanumFont"
          color="#3e9278"
          block
          dark
          >
            로그아웃
          </v-btn>
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
    NaverLogin
  },
  data () {
    return {
      dialog: false,
      img: '',
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
  mounted () {
    if (this.$store.state.user_jwt) {
      this.state = false
      this.username = this.$store.state.user_name
      let image = this.$store.state.user_image
      if (image.split('/').slice(3).join('/')) {
        this.img = 'https://' + image.split('/').slice(3).join('/')
      } else {
        this.img = require('../assets/user.png')
      }
    }
  },
  watch: {
    group () {
      this.drawer = false
    }
  },
  methods: {
    stop () {
      window.open(
        'http://localhost:8080/notWorking', 'window팝업',
        'width=700, height=700, menubar=no, status=no, toolbar=no'
      )
    },
    logout () {
      let scope = this
      Kakao.Auth.logout(function () {
        scope.$store.commit('jwtSave', '')
        scope.$store.commit('idSave', '')
        scope.$store.commit('nameSave', '')
        scope.$store.commit('pointSave', '')
        scope.$store.commit('gradeSave', '')
        scope.$store.commit('imgSave', '')
        Kakao.cleanup()
        scope.$router.push({ name: 'home' })
        location.reload()
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
  cursor pointer

#userrouter
  cursor pointer
  font-weight bold
  position relative

#userrouter:hover
  background #fff

#userrouter:before, #userrouter:after
  content ''
  position absolute
  bottom 0
  left 0
  height 1px
  width 0
  background #000
  transition 400ms ease all

#userrouter:hover:before, #userrouter:hover:after
  width 100%
  transition 800ms ease all

#logo:hover
  width 96px
  height 96px
  transition 400ms ease all
</style>
