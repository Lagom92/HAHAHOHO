<template>
    <div>
        <v-container>
            <v-row>
                <v-btn @click="Chk()">확인</v-btn>
                <div id="kakao-login-btn"></div>
                <a href="http://developers.kakao.com/logout"></a>
            </v-row>
        </v-container>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'KakaoLogin',
    data () {
        return {
            authObj: ''
        }
    },
    mounted() {
        let baseUrl = this.$store.state.baseUrl
        Kakao.init('b9b23d9b337a41dca3e1632a4677e0af');
        Kakao.Auth.createLoginButton({
            container: '#kakao-login-btn',
            success: this.authObj = function(authObj) {
                console.log(authObj)
                return authObj
            },
            fail: function(err) {
                console.log(err)
            }
        })
    },
    methods: {

    }
}
</script>

<style>
</style>