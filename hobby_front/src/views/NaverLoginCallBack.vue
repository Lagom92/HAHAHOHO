<template>
  <div>
  </div>
</template>

<script>
export default {
  name: 'naverLoginCallBack',
  data () {
    return {
      naver_id_login: '',
      access_token: '',
      userNickName: '',
      userName: '',
      userImage: '',
      userSex: '',
      userAge: '',
      userId: '',
      jwt: ''
    }
  },
  mounted () {
    this.naver_id_login = new naver_id_login(
      'IaquHgHTmPlf_gc_a8es',
      'http://localhost:8080/login/'
    )
    // 접근 토큰 값 출력
    this.$store.access_token = this.naver_id_login.oauthParams.access_token
    // 네이버 사용자 프로필 조회
    // this.naverLogin();
    this.temp()
  },
  methods: {
    async temp () {
      await this.naver_id_login.get_naver_userprofile(this.setInfo())
      await this.getInfo()
    },
    // 1. 백서버에 로그인 요청 (access_toekn + code)
    naverLogin () {
      this.$http.post(this.$store.state.baseUrl + 'accounts/rest-auth/naver/', {
        access_token: this.$store.access_token
      }).then(res => {
        this.jwt = res.data.token
        this.$store.jwt = res.data.token
      }).catch(e => {
        console.log(e)
      })
    },
    setInfo () {
      this.userNickName = this.naver_id_login.getProfileData('nickname')
      this.userName = this.naver_id_login.getProfileData('name')
      this.userSex = this.naver_id_login.getProfileData('gender')
      this.userAge = this.naver_id_login.getProfileData('age')
      this.userImage = this.naver_id_login.getProfileData('profile_image')
      this.userId = this.naver_id_login.getProfileData('id')
      this.getInfo()
    },
    // 2. 네이버에 사용자 프로필 정보 요청
    getInfo () {
      let baseUrl = this.$store.state.base_url
      let form = new FormData()
      console.log(this.userNickName,
        this.userName,
        this.userSex,
        this.userAge,
        this.userImage,
        this.userId
      )
      form.append('userNickName', this.userNickName)
      form.append('userName', this.userName)
      form.append('userSex', this.userSex)
      form.append('userAge', this.userAge)
      form.append('userImage', this.userImage)
      form.append('userId', 'naver_' + this.userId.toString())
      // this.$http.post(baseUrl+'accounts/userSave/', {
      //     headers:{
      //         'Authorization':'Jwt '+this.jwt
      //     },
      //     form
      // }).then(res =>{
      //     console.log(res)
      // }).catch(e =>{
      //     console.log(e)
      // })
    }
  }
}
</script>
