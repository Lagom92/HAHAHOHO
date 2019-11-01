<template>
  <div>
    <div id="kakao-login-btn"></div>
    <a href="http://developers.kakao.com/logout"></a>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'KakaoLogin',
  data () {
    return {
      jwt: '',
      id: '',
      user_id: '',
    }
  },
  mounted () {
    let scope = this
    Kakao.Auth.createLoginButton({
      container: '#kakao-login-btn',
      success: function (authObj) {
        Kakao.API.request({
          url: '/v2/user/me',
          success: function (res) {
            scope.userSave(authObj, res)
            return res
          },
          fail: function (error) {
            alert(JSON.stringify(error))
          }
        })
      },
      fail: function (err) {
        console.log(err)
      }
    })
  },
  methods: {
    async userSave (authObj, res) {
      let baseUrl = 'http://localhost:8000/'
      let accessToken = authObj.access_token
      let form = new FormData()
      form.append('access_token', accessToken)

      await axios.post(baseUrl + 'accounts/rest-auth/kakao', form).then(res => {
        this.jwt = res.data.token
        this.$store.commit('jwtSave', this.jwt)
      }).catch(e => {
        console.log(e)
      })
      this.id = 'kakao_' + (res.id).toString()
      
      let userForm = new FormData()
      userForm.append('userName', res.kakao_account.profile.nickname)
      userForm.append('userNickName', res.kakao_account.profile.nickname)
      userForm.append('userId', 'kakao_' + (res.id).toString())
      userForm.append('userSex', res.kakao_account.gender)
      userForm.append('userAge', res.kakao_account.age_range)
      userForm.append('userImage', res.kakao_account.profile.profile_image_url)
      this.$store.commit('nameSave', res.kakao_account.profile.nickname)

      await axios.post(baseUrl + 'accounts/userSave', userForm).then(res => {
        console.log(res.data)
      })
      await axios.post(baseUrl + 'accounts/userInfo', {
        // headers: { 'Authorization': 'JWT ' + this.jwt },
        id: this.id
      }).then(res => {
        this.user_id = res.data.id
        this.$store.commit('idSave', this.user_id)
      })      
      location.reload()
    }
  }
}
</script>
