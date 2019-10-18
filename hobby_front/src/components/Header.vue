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
export default {
  name: 'Header',
  data () {
    return {
      dialog: false,
    }
  },
  methods: {
    kakaologin() {
      Kakao.init('b9b23d9b337a41dca3e1632a4677e0af');
      Kakao.Auth.createLoginButton({
        container: '#kakao-login-btn',
        success: function(authObj) {
          alert(JSON.stringify(authObj));
        },
        fail: function(err) {
          alert(JSON.stringify(err));
        }
      });
    },
    naverlogin() {
      var naver_id_login = new naver_id_login("IaquHgHTmPlf_gc_a8es", "http://localhost:8080/callback");
      var state = naver_id_login.getUniqState();
      naver_id_login.setButton("white", 2,40);
      naver_id_login.setDomain("http://localhost:8080/");
      naver_id_login.setState(state);
      naver_id_login.setPopup();
      naver_id_login.init_naver_id_login();
    },
    naverlogincallback() {
      var naver_id_login = new naver_id_login("IaquHgHTmPlf_gc_a8es", "http://127.0.0.1:8000/account/rest-auth/naver/callback");
      // 접근 토큰 값 출력
      alert(naver_id_login.oauthParams.access_token);
      // 네이버 사용자 프로필 조회
      naver_id_login.get_naver_userprofile("naverSignInCallback()");
      // 네이버 사용자 프로필 조회 이후 프로필 정보를 처리할 callback function
      function naverSignInCallback() {
        alert(naver_id_login.getProfileData('email'));
        alert(naver_id_login.getProfileData('nickname'));
        alert(naver_id_login.getProfileData('age'));
      }
    }
  }
}
</script>

