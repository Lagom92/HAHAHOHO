<template>
    <div>
        <v-container>
            <v-btn @click="kakaologin">카카오로그인</v-btn>
            <div id="kakao-login-btn"></div>
            <a href="http://developers.kakao.com/logout"></a>
        </v-container>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'KakaoLogin',
    data () {
        return {
            accesstoken: ''
        }
    },
    methods: {
        kakaologin() {
            // baseUrl 부분은 서버 배포시 수정해야 하는 부분이기 때문에 store에 저장해서 가저오는게 하나로 관리하기가 편할것 같습니다.
            let baseUrl = "http://127.0.0.1:8000/"
            Kakao.init('b9b23d9b337a41dca3e1632a4677e0af');
            Kakao.Auth.createLoginButton({
                container: '#kakao-login-btn',
                success: function(authObj) {
                this.accesstoken = authObj.access_token;
                let form = new FormData()
                form.append('access_token', this.accesstoken)
                /*
                access_token으로 jwt 얻기 
                jwt로 권한 인증
                */ 
                axios.post(baseUrl+"accounts/rest-auth/kakao/", form)
                    .then((res) => {
                    // 여기 결과는 jwt 토큰 반환
                    console.log("jwt: ", res)
                    }).catch((e) => {
                    console.log(e)
                    })
                /*
                access_token으로 유저 정보 얻기
                */
                axios.post(baseUrl+"accounts/kakaoLogin/", form)
                    .then(res =>{
                    /* 
                    여기 결과는 유저 정보가 나옴
                    유저 id store에 저장해서 header나 페이지에서 닉네임? 확인 가능하게
                    payment에도 유저 id가 필요
                    */ 
                    console.log("유저정보: ", res)
                    }).catch(e =>{
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

<style>
</style>