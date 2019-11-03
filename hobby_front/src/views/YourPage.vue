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
                                        <v-img :src="item.img"></v-img>
                                      </v-list-item-avatar>
                                      <v-list-item-content>
                                        <v-list-item-title v-text="item.name">
                                        </v-list-item-title>
                                      </v-list-item-content>
                                    </v-list-item>
                                  </v-list>
                                  <v-list v-else>
                                    <v-list-item-content>
                                        <h3>팔로워가 없습니다 !</h3>
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
                                        <v-img :src="item.img"></v-img>
                                      </v-list-item-avatar>
                                      <v-list-item-content>
                                        <v-list-item-title v-text="item.name">
                                        </v-list-item-title>
                                      </v-list-item-content>
                                    </v-list-item>
                                  </v-list>
                                  <v-list v-else>
                                    <h3>팔로잉한 사람이 없습니다 !</h3>
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
        <v-timeline align-top :dense="$vuetify.breakpoint.smAndDown">
            <v-timeline-item
            v-for="(meet, i) in meets"
            :key="i"
            color="#EE7785"
            >
            <template v-slot:opposite>
                <span
                :class="`headline font-weight-bold ${meet.color}--text`"
                v-text="meet.day"
                ></span>
            </template>
            <v-card class="elevation-2">
                <v-card-title class="headline">{{meet.title}}</v-card-title>
                <v-card-text>
                    <p>{{meet.content}}</p>
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
  mounted(){
    this.getUserInfo(this.$route.params.id)
  },
  methods: {
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
        var strArray = res.data.userLike.split(',')
        this.tags = strArray
        let image = res.data.userImage
        let counts = image.length
        image = image.substr(14, counts)
        this.userInfo.userImage = 'https://'+image
        this.grade = require('../assets/' + this.userInfo.userGrade + '.png')
      })
      this.$http.get(this.$store.state.baseUrl + 'accounts/follows/' + id).then(res =>{
        this.followCounting = res.data.length
        for(let i of res.data){
          if(i.img == null){
            i.img = require('../assets/logo.png')
          }
        }
        this.followGroup = res.data    
      })
      this.$http.get(this.$store.state.baseUrl + 'accounts/followers/' + id).then(res =>{
        this.followerCounting = res.data.length
        for(let i of res.data){
          if(i.img == 'undefined'){
            i.img = require('../assets/logo.png')
          }
        }
        this.followerGroup = res.data 
      })
      let event = []
      let counts = 0
      this.$http.get(this.$store.state.baseUrl+'boards/participantCheckListByUser/' + id).then(res =>{
        let band = res.data
        let timeInMs = Date.now()
        for(let i in band){
          counts = counts + 1
          if(timeInMs > band[i].endDay){}
            console.log(band[i].endDay)
            let moim = {
              day: this.formatDate(band[i].created_at),
              color: 'indigo',
              icon: 'mdi-star',
              title: band[i].title,
              content: band[i].contents
            }
            event.push(moim)
          this.bandCount = counts
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
</style>
