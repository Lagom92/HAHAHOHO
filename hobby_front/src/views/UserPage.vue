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
                    <v-img
                    :src="userInfo.userImage"
                    max-height="100px"
                    max-width="100px"
                    class="mx-auto"
                    ></v-img>
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
                    src="../assets/logo.png"
                    max-height="100px"
                    max-width="100px"
                    class="mx-auto"
                    ></v-img>(등급아이콘자리)
                    <v-list-item-title class="headline mb-1 text-center">
                      <v-row justify="center">
                        <span class="my-auto mr-3">포인트 {{userInfo.userPoint}}P</span>
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
                                  <v-list>
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
                                  <v-list>
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
                    <v-toolbar-title v-html="selectedEvent.name"></v-toolbar-title>
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
      var strArray = res.data.userLike.split(',')
      this.tags = strArray
      // 카카오만
      image = image.substr(14, counts)
      this.userInfo.userImage = 'https://'+image
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
    let scope = this
    let event = []
    let counts = 0
    this.$http.get(this.$store.state.baseUrl+'boards/participantCheckListByUser/'+this.$store.state.user_id).then(res =>{
      let band = res.data
      let timeInMs = Date.now()
      let selectColor
      let detail
      for(let i in band){
         if(timeInMs < Date.parse(band[i].endDay)){
          selectColor = '#ff7473'
        } else {
          selectColor = '#60c5ba'
        }
        detail = {
          startDay: band[i].startDay,
          startTime: band[i].startTime,
          location: band[i].location,
          fee: band[i].fee
        }
        let moim = {
          name: band[i].title,
          details: detail,
          start: band[i].startDay,
          end: band[i].endDay,
          color: selectColor,
        }
        event.push(moim)
        counts = counts + 1
        this.bandCount = counts
      }
    }).catch(e =>{
      console.log(e)
    })
    this.events = event
  },
  methods: {
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
  }
}
</script>

<style lang="stylus">
#contain_card
  width 100%
</style>
