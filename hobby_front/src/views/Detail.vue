<template>
  <div>
    <v-container>
      <v-row>
        <v-col cols="12" md="5">
          <v-chip small color="#9AB878" dark>{{data.subclassname}}</v-chip>
          <h1>{{data.title}}</h1>
          <p>작성 날짜: {{data.created_at}}</p>
        </v-col>
        <v-col cols="12" md="2">
          <v-menu
          transition="scale-transition"
          >
            <template v-slot:activator="{ on }">
              <v-chip pill v-on="on" class="mt-8">
                <v-avatar left>
                  <v-img :src="data.userimage"></v-img>
                </v-avatar>
                {{data.username}}
              </v-chip>
            </template>
            <v-card width="300">
              <v-list dark>
                <v-list-item>
                  <v-list-item-avatar>
                    <v-img :src="data.userimage"></v-img>
                  </v-list-item-avatar>
                  <v-list-item-content>
                    <v-list-item-title>{{data.username}}</v-list-item-title>
                    <v-list-item-subtitle>친절함 활발함</v-list-item-subtitle>
                  </v-list-item-content>
                  <v-list-item-action>
                    <v-btn icon >
                      <v-icon>mdi-chevron-right</v-icon>
                    </v-btn>
                  </v-list-item-action>
                </v-list-item>
              </v-list>
            </v-card>
          </v-menu>
        </v-col>
        <!-- 유저의 상태에 따라 변경되야함 -->
        <v-col cols="12" md="4" offset-md="1" class="d-flex align-center" >
          <v-btn block dark color="#F3B749">참여하기</v-btn>
        </v-col>
        <div class="mb-4 mr-4">
          모집 마감: 
          <v-icon class="mr-1">mdi-calendar-month</v-icon>
          {{data.startDay}}
        </div>
        <div class="mb-4">
          <v-icon class="mr-1">mdi-clock-outline</v-icon>
          {{data.startTime}}
        </div>
      </v-row>
      <v-row>
        <v-col cols="12" md="7">
          <v-img
          :src= "data.photo"
          class="mb-12"
          ></v-img>
          <v-card class="excard">
            <v-card-title class="mb-3">
              모임 소개
            </v-card-title>
            <v-card-text class="text--primary">
              <div>
                {{data.contents}}
              </div>
            </v-card-text>
          </v-card>
        </v-col>
        <v-col cols="12" md="4" offset-md="1">
          <v-card class="excard">
            <v-card-title class="mb-3">
              모임 정보
            </v-card-title>
            <v-card-text class="text--primary">
              
              <div class="mb-4">
                <v-icon class="mr-1">mdi-calendar-month</v-icon>
                날짜: {{data.startDay}}
              </div>
              <div class="mb-4">
                <v-icon class="mr-1">mdi-clock-outline</v-icon>
                시각: {{data.startTime}}
              </div>
              <div class="mb-4">
                <v-icon class="mr-1">mdi-map-marker</v-icon>
                장소: {{data.location}}
              </div>
              <div class="mb-4">
                <v-icon class="mr-1">mdi-account</v-icon>
                인원: 최대 {{data.member}}명 / {{data.minAge}}세 ~ {{data.maxAge}}세까지
              </div>
              <div class="mb-4">
                <v-icon class="mr-1">mdi-gender-male-female</v-icon>
                {{data.gender}}
              </div>
              <div class="mb-4">
                <v-icon class="mr-1">mdi-currency-krw</v-icon>
                예상 비용: {{data.fee}}원
              </div>
            </v-card-text>
          </v-card>
          <div class="mb-12" id="mapview">
            <!-- 지도 -->
            <!-- <MapService :address="location"></MapService>   -->
            <MapService></MapService>  
          </div>
          <v-card class="excard">
            <div id="member">
              <v-card-title class="mb-3">
                모임 멤버 (1 / 10)
              </v-card-title>
              <v-chip pill class="ma-3">
                <v-avatar left>
                  <v-img :src="data.userimage"></v-img>
                </v-avatar>
                {{data.username}}
              </v-chip>
            </div>
          </v-card>
        </v-col>
      </v-row>
      <!-- 댓글 -->
      <CommentHobby class="mt-10"></CommentHobby>
    </v-container>
  </div>
</template>

<script>
import MapService from '../components/MapService'
import CommentHobby from '../components/CommentHobby'

export default {
  name: 'Detail',
  components: {
    MapService,
    CommentHobby

  },
  data () {
    return {
      data: {age: [0,0]},
      id: '',
    }
  },
  mounted () {
    this.id = this.$route.params.id
    this.get_detail();
},
  methods: {
    get_detail: function () {
      const baseUrl = this.$store.state.baseUrl
      const apiUrl = baseUrl + 'boards/hobby/' + this.id
      this.$http.get(apiUrl)
      .then(res => {
        let created_at = res.data.created_at
        let startTime = res.data.startTime
        let endTime = res.data.endTime 
        let startDay = res.data.startDay
        let endDay = res.data.endDay

        res.data.startTime = startTime.substring(0,2)+'시 '+startTime.substring(3,5)+'분'  
        res.data.endTime = endTime.substring(0,2)+'시 '+endTime.substring(3,5)+'분'
        res.data.created_at = created_at.substring(0,4)+'년 '+created_at.substring(5,7)+'월 '+created_at.substring(8,10)+'일' 
        res.data.startDay = startDay.substring(0,4)+'년 '+ startDay.substring(5,7)+'월 '+startDay.substring(8,10)+'일'
        res.data.endDay = endDay.substring(0,4)+'년 '+ endDay.substring(5,7)+'월 '+endDay.substring(8,10)+'일'

        res.data.fee = res.data.fee.toLocaleString()

        this.data = res.data        
      })
      .catch(err => {
        console.log(err)
      })
    }
  }

}
</script>

<style lang="stylus">
.excard
  margin-bottom 48px

#leader
  height 50%

#member
  height 50%

#mapview
  height 300px
</style>
