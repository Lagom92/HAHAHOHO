<template>
    <div>
        <v-container>
            <v-btn><a :href="naverLoginURL">네이버</a></v-btn>
        </v-container>
    </div>
</template>

<script>
import axios from 'axios'

// var naver_id_login = new naver_id_login("IaquHgHTmPlf_gc_a8es", "http://localhost:8080/");
// var state = naver_id_login.getUniqState();
// naver_id_login.setButton("white", 2,40);
// naver_id_login.setDomain("http://127.0.0.1:8000/");
// naver_id_login.setState(1);
// naver_id_login.setPopup();
// naver_id_login.init_naver_id_login();


export default {
    name: 'NaverLogin',
    data () {
        return {
            CLIENT_ID: 'IaquHgHTmPlf_gc_a8es',
            redirectURI: 'http://127.0.0.1:8000/accounts/naverLogin',
            //  FIXME state 값 random string 으로 변경
            state: 123,
            naverLoginURL: 'https://nid.naver.com/oauth2.0/authorize?response_type=code'
        }
    },
    created () {
        this.naverLoginURL += '&client_id=' + this.CLIENT_ID
        this.naverLoginURL += '&redirect_uri=' + this.redirectURI
        this.naverLoginURL += '&state=' + this.state
    },
    // methods: {
    //     naverLogin() {
        //     let baseUrl = "http://127.0.0.1:8000/"
        //     let clientId = "IaquHgHTmPlf_gc_a8es"
        //     let clientSecret = "nUsvfl0B6c"
        //     let state = 1010
        //     let redirectURI = encodeURI("http://localhost:8080/")
        //     let api_url = ""
        //     api_url = 'https://nid.naver.com/oauth2.0/authorize?response_type=code&client_id=' + clientId + '&redirect_uri=' + redirectURI + '&state=' + state;
        //     axios.get(api_url, {
        //         headers: {
        //             'Content-Type': 'text/html;charset=utf-8'
        //         }
        //     })
        //     .then(res =>{
        //         console.log(res)
        //     }).catch(e => {
        //         console.log(e)
        //     })
    //     }
    // }
}
</script>

<style>
</style>