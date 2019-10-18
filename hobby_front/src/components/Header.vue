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
            <v-btn @click="kakaologin">카카오로그인</v-btn>
            <div id="kakao-login-btn"></div>
            <a href="http://developers.kakao.com/logout"></a>
          </v-col>
        </v-row>
      </v-container>
    </v-toolbar>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Header',
  data () {
    return {
      dialog: false,
      accesstoken: '',
    }
  },
  methods: {
    kakaologin() {
      Kakao.init('b9b23d9b337a41dca3e1632a4677e0af');
      Kakao.Auth.createLoginButton({
        container: '#kakao-login-btn',
        success: function(authObj) {
          this.accesstoken = authObj.access_token;
          axios.post('http://127.0.0.1:8000/accounts/rest-auth/kakao/', {body: this.accesstoken})
          .then((res) => {
            console.log(res)
          }).catch((e) => {
            console.log(e)
          })
        },
        fail: function(err) {
          alert(JSON.stringify(err));
        }
      });
    }
  }
}
</script>
