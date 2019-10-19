<template>
  <div>
    <v-toolbar fixed>
      <v-container>
        <v-row>
          <v-col md="2">
            <v-toolbar-title>하하호호</v-toolbar-title>
          </v-col>

          <v-col md="3">
            <v-btn text>모임</v-btn>
            <v-btn text>커뮤니티</v-btn>
          </v-col>

          <v-col md="2" offset-md="5">
            <!-- 카카오로그인 버튼 노출 영역 -->
            <KakaoLogin></KakaoLogin>
          </v-col>
        </v-row>
      </v-container>
    </v-toolbar>
  </div>
</template>

<script>
import KakaoLogin from '@/components/KakaoLogin'

export default {
  name: 'Header',
  data () {
    return {
      dialog: false
    }
  },
  components: {
    KakaoLogin
  }
}
</script>
