<template>
  <div>
    <v-container>
      <div>
        <v-row align="center">
          <v-card id="contain_card" class="my-10">
            <v-row>
              <v-card
              class="mx-auto my-auto"
              max-width="344"
              elevation="0"
              >
                <v-list-item three-line>
                  <v-list-item-content>
                    <v-avatar size="150">
                      <img
                        :src="userInfo.userImage"
                      >
                    </v-avatar>
                    <v-list-item-title class="headline mb-1 text-center">
                      {{userInfo.userName}}
                      <v-btn
                      class="ma-2"
                      color="#9AB878"
                      small
                      dark
                      outlined
                      @click="addFollow"
                      v-if="followState"
                      >
                        팔로잉
                      </v-btn>
                      <v-btn
                      class="ma-2"
                      color="#9AB878"
                      small
                      dark
                      @click="addFollow"
                      v-else
                      >
                        팔로우
                      </v-btn>
                    </v-list-item-title>
                    <v-list-item-subtitle class="text-center">
                      <div>
                        <v-chip
                        v-for="i in tags"
                        :key="i"
                        class="ma-1"
                        color="#F3B749"
                        text-color="white"
                        >
                          {{i}}
                        </v-chip>
                      </div>
                    </v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
              </v-card>
              <v-divider class="my-5" vertical></v-divider>
              <v-card
              class="mx-auto my-auto"
              max-width="344"
              elevation="0"
              >
                <v-list-item three-line>
                  <v-list-item-content>
                    <v-img
                    :src="grade"
                    max-height="100px"
                    max-width="100px"
                    class="mx-auto"
                    ></v-img>
                    <v-list-item-subtitle class="text-center">
                      <div>
                        <v-row>
                          <v-col cols="4" >
                            <span>참여모임 {{bandCount}}</span>
                          </v-col>
                          <v-col cols="4">
                            <v-dialog
                            v-model="followerdialog"
                            scrollable
                            max-width="300px"
                            >
                              <template v-slot:activator="{ on }">
                                <span v-on="on">팔로워 {{followerCounting}}</span>
                              </template>
                              <!-- 팔로워 목록 모달 -->
                              <v-card>
                                <v-card-title>팔로워</v-card-title>
                                <v-divider></v-divider>
                                <v-card-text style="height: 300px;">
                                  <v-list v-if="followerCounting">
                                    <v-list-item 
                                    v-for="item in followerGroup"
                                    :key="item.name"
                                    >
                                      <v-list-item-avatar>
                                        <v-img @click="move(item.id)" :src="item.img"></v-img>
                                      </v-list-item-avatar>
                                      <v-list-item-content>
                                        <v-list-item-title id="link" @click="move(item.id)" v-text="item.name">
                                        </v-list-item-title>
                                      </v-list-item-content>
                                    </v-list-item>
                                  </v-list>
                                  <v-list v-else>
                                    <v-list-item-content>
                                        <h3 id="center">팔로워가 없습니다 !</h3>
                                      </v-list-item-content>
                                  </v-list>
                                </v-card-text>
                                <v-divider></v-divider>
                                <v-card-actions>
                                  <v-btn
                                  color="#2E1E11"
                                  text
                                  @click="followerdialog = false"
                                  >
                                    Close
                                  </v-btn>
                                </v-card-actions>
                              </v-card>
                            </v-dialog>
                          </v-col>
                          <v-col cols="4">
                            <v-dialog
                            v-model="followdialog"
                            scrollable
                            max-width="300px"
                            >
                              <template v-slot:activator="{ on }">
                                <span v-on="on">팔로잉 {{followCounting}}</span>
                              </template>
                              <!-- 팔로우 목록 모달 -->
                              <v-card>
                                <v-card-title>팔로잉</v-card-title>
                                <v-divider></v-divider>
                                <v-card-text style="height: 300px;">
                                  <v-list v-if="followCounting">
                                    <v-list-item
                                    v-for="item in followGroup"
                                    :key="item.title"
                                    >
                                      <v-list-item-avatar>
                                        <v-img @click="move(item.id)" :src="item.img"></v-img>
                                      </v-list-item-avatar>
                                      <v-list-item-content>
                                        <v-list-item-title id="link" @click="move(item.id)" v-text="item.name">
                                        </v-list-item-title>
                                      </v-list-item-content>
                                    </v-list-item>
                                  </v-list>
                                  <v-list v-else>
                                    <h3 id="center">팔로잉한 사람이 없습니다 !</h3>
                                  </v-list>
                                </v-card-text>
                                <v-divider></v-divider>
                                <v-card-actions>
                                  <v-btn
                                  color="#2E1E11"
                                  text
                                  @click="followdialog = false"
                                  >
                                    Close
                                  </v-btn>
                                </v-card-actions>
                              </v-card>
                            </v-dialog>
                          </v-col>
                        </v-row>
                      </div>
                    </v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
              </v-card>
            </v-row>
          </v-card>
        </v-row>
      </div>
      <!-- 유저가 참여한 목록 -->
      <div>
        <div>
          <h2 class="no-background"><span>{{userInfo.userNickName}}의 타임라인</span></h2>
        </div>
        <v-timeline align-top :dense="$vuetify.breakpoint.smAndDown">
            <v-timeline-item
            v-for="(meet, i) in meets"
            :key="i"
            color="#EE7785"
            >
            <v-card class="elevation-2">
                <v-card-title class="headline">{{meet.title}}</v-card-title>
                <v-card-text>
                  <v-row>
                    <v-col cols="3">
                      <v-img :src="meet.photo" height="100"></v-img>
                    </v-col>
                    <v-col cols="9">
                      <div class="mb-4">
                        <v-icon class="mr-1">mdi-calendar-month</v-icon>
                        날짜 : {{meet.meetDay}}
                      </div>
                      <div class="mb-4">
                        <v-icon class="mr-1">mdi-map-marker</v-icon>
                        장소 : {{meet.location}}
                      </div>
                      <div class="mb-4">
                        <v-icon class="mr-1">mdi-text</v-icon>
                        내용 : {{meet.content}}
                      </div>
                    </v-col>
                  </v-row>
                </v-card-text>
            </v-card>
            </v-timeline-item>
        </v-timeline>
      </div>
    </v-container>
  </div>
</template>

<script>
import Payment from '@/components/Payment'

export default {
  name: 'UserPage',
  components: {
    Payment
  },
  data () {
    return {
      followState: false,
      grade:'',
      followCounting: 0,
      followerCounting: 0,
      followGroup:[],
      followerGroup:[],
      followdialog: false,
      followerdialog: false,
      bandCount:0,
      userInfo:{
        'id': 0,
        'userAddress': "",
        'userAge': "",
        'userGrade': 0,
        'userId': "",
        'userImage': "",
        'userLike': "",
        'userName': "",
        'userNickName': "",
        'userPoint': 0,
        'userSex': "",
      },
      tags:[
        "카테고리를 선택하지 않았습니다."
      ],
      meets: [
      ],
    }
  },
  watch:{
    followState: function(){
      this.followInfo(this.userInfo.id)
      this.followerInfo(this.userInfo.id)
    }
  },
  mounted(){
    this.getUserInfo(this.$route.params.id)
    this.followInfo(this.$route.params.id)
    this.followerInfo(this.$route.params.id)
  },
  methods: {
    move(id){
      if(id == this.$store.state.user_id){
        this.$router.push({name: 'user'})
      } else {
        this.$router.push({name: 'yourpage', params:{id:id}})
      }
    },
    followInfo(id){
      this.$http.get(this.$store.state.baseUrl + 'accounts/follows/' + id).then(res =>{
        this.followCounting = res.data.length
        for(let i of res.data){
          if(i.img == null){
            i.img = require('../assets/logo.png')
          }
        }
        this.followGroup = res.data    
      })
    },
    followerInfo(id){
      this.$http.get(this.$store.state.baseUrl + 'accounts/followers/' + id).then(res =>{
        this.followerCounting = res.data.length
        for(let i of res.data){
          if(i.name == this.$store.state.user_name){
            this.followState = true
          }
          if(i.img == 'undefined'){
            i.img = require('../assets/logo.png')
          }
        }
        this.followerGroup = res.data 
      })
    },
    addFollow(){
      this.$http.post(this.$store.state.baseUrl + "accounts/following/" + this.$store.state.user_id + "/" + this.userInfo.id).then(res =>{
        if(this.followState){
          this.followState = false
        } else {
          this.followState = true
        }
      })
    },
    formatDate(date) {
      var d = new Date(date),
          month = '' + (d.getMonth() + 1),
          day = '' + d.getDate(),
          year = d.getFullYear();

      if (month.length < 2) 
          month = '0' + month;
      if (day.length < 2) 
          day = '0' + day;

      return [year, month, day].join('-');
    },
    getUserInfo(id){
      let form = new FormData()
      form.append('id', id)
      this.$http.post(this.$store.state.baseUrl + "accounts/userInfo", form).then(res =>{
        this.userInfo = res.data
        if(res.data.userLike != ""){
          var strArray = res.data.userLike.split(',')
          this.tags = strArray
        }
        let image = res.data.userImage
        let counts = image.length 
        if(image.split('/').slice(3).join('/')){
          this.userInfo.userImage = 'https://' + image.split('/').slice(3).join('/')
        } else {
          this.userInfo.userImage = require('../assets/user.png')
        }
        this.grade = require('../assets/' + this.userInfo.userGrade + '.png')
      })
      let event = []
      let counts = 0
      this.$http.get(this.$store.state.baseUrl+'boards/participantCheckListByUser/' + id).then(res =>{
        let band = res.data
        let timeInMs = Date.now()
        for(let i in band){
          counts = counts + 1
          if(timeInMs > new Date(band[i].endDay)){
            let photo = band[i].photo
            photo = photo.substr(1)
            let moim = {
              day: this.formatDate(band[i].created_at),
              color: 'indigo',
              icon: 'mdi-star',
              title: band[i].title,
              content: band[i].contents,
              photo: this.$store.state.baseUrl + photo,
              meetDay: band[i].startDay,
              location: band[i].location
            }
            event.push(moim)
            this.bandCount = counts
          }
        }
      })
      this.meets = event
    }
  }
}
</script>

<style lang="stylus">
#contain_card
  width 100%

h2 {
    font: 33px sans-serif;
    margin-top: 30px;
    text-align: center;
    text-transform: uppercase;
}

h2.no-background {
    position: relative;
    overflow: hidden;
    
    span {
        display: inline-block;
        vertical-align: baseline;
        zoom: 1;
        *display: inline;
        *vertical-align: auto;
        position: relative;
        padding: 0 20px;

        &:before, &:after {
            content: '';
            display: block;
            width: 1000px;
            position: absolute;
            top: 0.73em;
        }

        &:before { right: 100%; }
        &:after { left: 100%; }
    }
}

#center{
  text-align:center;
  margin-top:130px
}
#link
  cursor pointer
</style>
