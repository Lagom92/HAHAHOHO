<template>
    <div>
        <v-container>
            <v-row>
                <div id="kakao-login-btn"></div>
                <a href="http://developers.kakao.com/logout"></a>
            </v-row>
            <v-btn @click="Chk()">확인</v-btn>
        </v-container>
    </div>
</template>

<script>
import axios from 'axios'
import { access } from 'fs'

export default {
    name: 'KakaoLogin',
    data () {
        return {
            jwt:'',
            id:''
        }
    },
    mounted() {
        let scope = this
        let baseUrl = this.$store.state.baseUrl
        Kakao.init('b9b23d9b337a41dca3e1632a4677e0af');
        Kakao.Auth.createLoginButton({
            container: '#kakao-login-btn',
            success: function(authObj) {
                Kakao.API.request({
                    url: '/v2/user/me',
                    success: function(res) {
                        scope.userSave(authObj, res)
                        return res
                    },
                    fail: function(error) {
                        alert(JSON.stringify(error));
                    }
                });
            },
            fail: function(err) {
                console.log(err)
            }
        })
    },
    methods: {
        userSave(authObj, res){
            let baseUrl = 'http://localhost:8000/'
            let access_token = authObj.access_token
            let form = new FormData()
            form.append('access_token', access_token)

            axios.post(baseUrl+'accounts/rest-auth/kakao/',form).then(res =>{
                this.jwt = res.data.token
            }).catch(e =>{
                console.log(e)
            })
            this.id = "kakao_"+ (res.id).toString()
            let userForm = new FormData()
            userForm.append('userName', res.kakao_account.profile.nickname)
            userForm.append('userNickName', res.kakao_account.profile.nickname)
            userForm.append('userId', "kakao_"+ (res.id).toString())
            userForm.append('userSex', res.kakao_account.gender)
            userForm.append('userAge', res.kakao_account.age_range)
            userForm.append('userImage', res.kakao_account.profile.profile_image_url)
            axios.post(baseUrl+'accounts/userSave/', userForm).then(res =>{
                console.log(res.data)
            })
        },
        // 이 부분은 유저 정보 사이트에 mounted로 넣어주면 될거같습니다.ㅇ
        Chk() {
            let baseUrl = 'http://localhost:8000/'
            axios.post(baseUrl + 'accounts/userInfo/', 
                {
                    headers: 
                        {'Authorization': 'JWT '+ this.jwt },
                    id:this.id
                }
            ).then(res =>{
                console.log(res)
            })
        }
    }
}
</script>

<style>
</style>