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
                    <v-avatar size="120">
                      <img
                        :src="userInfo.userImage"
                      >
                    </v-avatar>
                    <v-list-item-title class="headline mb-1 text-center">
                      {{userInfo.userNickName}}
                      <v-btn
                      class="ma-2"
                      color="#9AB878"
                      fab
                      outlined
                      x-small
                      dark
                      @click="$router.push('/userupdate')"
                      >
                        <v-icon>mdi-account-edit</v-icon>
                      </v-btn>
                    </v-list-item-title>
                    <v-list-item-subtitle class="text-center">
                      <div>
                        <v-chip
                        v-for="i in this.tags"
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
                    <v-list-item-title class="headline mb-1 text-center">
                      <v-row v-if="userInfo.userGrade == 1" justify="center">
                        <br><br>
                        <span  class="my-auto mr-3 body-2">유저정보를 수정해주시면 포인트가 <span class="font-weight-bold">팡팡!</span></span>
                      </v-row>
                      <v-row v-else justify="center">
                        <span  class="my-auto mr-3">포인트 {{userInfo.userPoint}}P</span>
                        <Payment></Payment>
                      </v-row>
                    </v-list-item-title>
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
                                        <v-list-item-title id="link" @click="move(item.id)"  v-text="item.name">
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
                                  class="ml-auto"
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
      <!-- 유저 달력 -->
      <div>
        <v-row class="fill-height">
          <v-col>
            <v-sheet height="64">
              <v-toolbar flat color="white">
                <v-btn text @click="setToday">
                  Today
                </v-btn>
                <v-spacer></v-spacer>
                <v-btn fab text small @click="prev">
                  <v-icon small>mdi-chevron-left</v-icon>
                </v-btn>
                <v-toolbar-title>{{ title }}</v-toolbar-title>
                <v-btn fab text small @click="next">
                  <v-icon small>mdi-chevron-right</v-icon>
                </v-btn>
                <v-spacer></v-spacer>
                <div>
                  <v-tooltip bottom>
                    <template v-slot:activator="{ on }">
                      <v-icon small color="#f9c00c" v-on="on" class="ma-1">mdi-circle</v-icon>
                    </template>
                    <span>찜하기</span>
                  </v-tooltip>
                  <v-tooltip bottom>
                    <template v-slot:activator="{ on }">
                      <v-icon small color="#60c5ba" v-on="on" class="ma-1">mdi-circle</v-icon>
                    </template>
                    <span>참여완료</span>
                  </v-tooltip>
                  <v-tooltip bottom>
                    <template v-slot:activator="{ on }">
                      <v-icon small color="#ff7473" v-on="on" class="ma-1">mdi-circle</v-icon>
                    </template>
                    <span>참여예정</span>
                  </v-tooltip>
                  <br>
                </div>
              </v-toolbar>
            </v-sheet>
            <v-sheet height="600">
              <v-calendar
                ref="calendar"
                v-model="focus"
                color="primary"
                :events="events"
                :event-color="getEventColor"
                :event-margin-bottom="3"
                @click:event="showEvent"
                @click:more="viewMore"
                @change="updateRange"
              ></v-calendar>
              <v-menu
                v-model="selectedOpen"
                :close-on-content-click="false"
                :activator="selectedElement"
                full-width
                offset-x
              >
                <v-card color="grey lighten-4" min-width="350px" flat >
                  <v-toolbar
                    :color="selectedEvent.color"
                    dark
                    flat
                  >
                    <v-btn icon>
                      <v-icon>mdi-bell-alert</v-icon>
                    </v-btn>
                    <v-toolbar-title id="link" @click="moveTo(selectedEvent.id)" v-html="selectedEvent.name"></v-toolbar-title>
                    <v-spacer></v-spacer>
                    <v-btn icon @click="selectedOpen = false">
                      <v-icon>mdi-close</v-icon>
                    </v-btn>
                  </v-toolbar>
                  <v-card-text>
                    <div class="mb-4">
                      <v-icon class="mr-1">mdi-calendar-month</v-icon>
                      {{selectedEvent.details.startDay}}
                    </div>
                    <div class="mb-4">
                      <v-icon class="mr-1">mdi-clock-outline</v-icon>
                      {{selectedEvent.details.startTime}}
                    </div>
                    <div class="mb-4">
                      <v-icon class="mr-1">mdi-map-marker</v-icon>
                      {{selectedEvent.details.location}}
                    </div>
                    <div class="mb-4">
                      <v-icon class="mr-1">mdi-currency-krw</v-icon>
                      {{selectedEvent.details.fee}}원
                    </div>
                  </v-card-text>
                </v-card>
              </v-menu>
            </v-sheet>
          </v-col>
        </v-row>
      </div>
    </v-container>
    <!-- Point 내역 -->
    <Bill></Bill>
    <KakaoBill></KakaoBill>
  </div>
</template>

<script>
import Payment from '@/components/Payment'
import Bill from '@/components/Bill'
import KakaoBill from '@/components/KakaoBill'


export default {
  name: 'UserPage',
  components: {
    Payment,
    Bill,
    KakaoBill
  },
  data () {
    return {
      grade:'',
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
      band:'',
      tags: [
        '카테고리를 선정해주세요'
      ],
      followCounting: 0,
      followerCounting: 0,
      followGroup:[],
      followerGroup:[],
      followdialog: false,
      followerdialog: false,
      items: [],
      today: new Date().toISOString(),
      focus: new Date().toISOString(),
      type: 'month',
      start: null,
      end: null,
      selectedEvent: {
        details : {
          startDay: '',
          startTime: '',
          location: '',
          fee: ''
        }
      },
      bandCount:0,
      selectedElement: null,
      selectedOpen: false,
      events:[],
    }
  },
  computed: {
    title () {
      const { start, end } = this
      if (!start || !end) {
        return ''
      }

      const startMonth = this.monthFormatter(start)
      const startYear = start.year

      return `${startYear}년 ${startMonth}`
    },
    monthFormatter () {
      return this.$refs.calendar.getFormatter({
        timeZone: 'UTC', month: 'long',
      })
    },
  },
  mounted () {
    this.$refs.calendar.checkChange()
    let headers = {
      'Authorization' : 'JWT '+this.$store.state.user_jwt
    }
    // user 프로필 정보
    let form = new FormData()
    let data = this.$store.state.user_id
    form.append('id', data)
    this.$http.post(this.$store.state.baseUrl+'accounts/userInfo', form).then(res =>{
      this.userInfo.id = res.data.id
      this.userInfo.userAddress = res.data.userAddress
      this.userInfo.userAge = res.data.userAge
      this.userInfo.userGrade = res.data.userGrade
      this.userInfo.userId = res.data.userId
      this.userInfo.userName = res.data.userName
      this.userInfo.userNickName = res.data.userNickName
      this.userInfo.userPoint = res.data.userPoint
      this.userInfo.userSex = res.data.userSex
      let image = res.data.userImage
      let counts = image.length
      if(res.data.userLike != ""){
        var strArray = res.data.userLike.split(',')
        this.tags = strArray
      }
      if(this.userInfo.userGrade > 1){
        this.grade = require('../assets/2.png')
      } else if(this.userInfo.userGrade > 100){
        this.grade = require('../assets/3.png')
      } else if(this.userInfo.userGrade > 500){
        this.grade = require('../assets/4.png')
      } else if(this.userInfo.userGrade > 1000){
        this.grade = require('../assets/5.png')
      }
      if(image.split('/').slice(3).join('/')){
        this.userInfo.userImage = 'https://' + image.split('/').slice(3).join('/')
      } else {
        this.userInfo.userImage = require('../assets/user.png')
      }
    }).catch(e =>{
      console.log(e)
    })
    // user 팔로잉(내가 하는거)
    this.$http.get(this.$store.state.baseUrl + 'accounts/follows/' + this.$store.state.user_id).then(res =>{
      this.followCounting = res.data.length
      for(let i of res.data){
        if(i.img == null){
          i.img = require('../assets/logo.png')
        }
      }
      this.followGroup = res.data
    })
    // user 팔로워(나를 하는거)
    this.$http.get(this.$store.state.baseUrl + 'accounts/followers/' + this.$store.state.user_id).then(res =>{
      this.followerCounting = res.data.length
      for(let i of res.data){
        if(i.img == 'undefined'){
          i.img = require('../assets/logo.png')
        }
      }
      this.followerGroup = res.data
    })
    // user가  참여모임에 대한 모든 정보
    let event = []
    let counts = 0
    this.$http.get(this.$store.state.baseUrl+'boards/participantCheckListByUser/'+this.$store.state.user_id).then(res =>{
      let band = res.data
      let timeInMs = Date.now()
      let selectColor
      for(let i in band){
         if(timeInMs < Date.parse(band[i].endDay)){
          selectColor = '#ff7473'
        } else {
          selectColor = '#60c5ba'
        }
        var detail = {
          startDay: band[i].startDay,
          startTime: band[i].startTime,
          location: band[i].location,
          fee: band[i].fee
        }
        var moim = {
          id: band[i].id,
          name: band[i].title,
          details: detail,
          start: band[i].startDay,
          end: band[i].startDay,
          color: selectColor,
        }
        event.push(moim)
        counts = counts + 1
        this.bandCount = counts
      }
    }).catch(e =>{
      console.log(e)
    })
    // 유저 찜 목록 추가
    this.$http.get(this.$store.state.baseUrl + "boards/cartList/" + this.$store.state.user_id).then(res =>{
      for(let i of res.data.post_id){
        this.$http.get(this.$store.state.baseUrl + "boards/hobby/" + i).then(r =>{
          let detail = {
          startDay: this.formatDate(r.data.created_at),
          startTime: r.data.startTime,
          location: r.data.location,
          fee: r.data.fee
          }
          let moim = {
            name: r.data.title,
            details: detail,
            start: this.formatDate(r.data.created_at),
            end: r.data.endDay,
            color: '#f9c00c'
          }
          event.push(moim)
        }).catch(e =>{
          console.log(e)
        })
      }
    }).catch(error =>{
      console.log(error)
    })
    this.events = event
  },
  methods: {
    moveTo(id){
      this.$router.push({name: 'detail', params:{id:id}})
    },
    move(id){
      this.$router.push({name: 'yourpage', params:{id:id}})
    },
    viewMore ({ date }) {
      this.focus = date
    },
    getEventColor (event) {
      return event.color
    },
    setToday () {
      this.focus = this.today
    },
    prev () {
      this.$refs.calendar.prev()
    },
    next () {
      this.$refs.calendar.next()
    },
    showEvent ({ nativeEvent, event }) {
      const open = () => {
        this.selectedEvent = event
        this.selectedElement = nativeEvent.target
        setTimeout(() => this.selectedOpen = true, 10)
      }

      if (this.selectedOpen) {
        this.selectedOpen = false
        setTimeout(open, 10)
      } else {
        open()
      }

      nativeEvent.stopPropagation()
    },
    updateRange ({ start, end }) {
      this.start = start
      this.end = end
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
    }
  }
}
</script>

<style lang="stylus">
#contain_card
  width 100%

#center{
  text-align:center;
  margin-top:130px
}
</style>

<style lang="stylus">
#link
  cursor pointer
</style>