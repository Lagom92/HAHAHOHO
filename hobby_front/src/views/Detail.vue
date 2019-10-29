<template>
  <div>
    <v-container>
      <v-row>
        <v-col cols="12" md="5">
          <v-chip small color="#9AB878" dark>{{data.subclassname}}</v-chip>
          <h1>{{data.title}}</h1>
        </v-col>
        <v-col cols="12" md="2">
          <v-menu
          transition="scale-transition"
          >
            <template v-slot:activator="{ on }">
              <v-chip pill v-on="on" class="mt-8">
                <v-avatar left>
                  <v-img src="https://cdn.vuetifyjs.com/images/john.png"></v-img>
                </v-avatar>
                {{data.username}}
              </v-chip>
            </template>
            <v-card width="300">
              <v-list dark>
                <v-list-item>
                  <v-list-item-avatar>
                    <v-img src="https://cdn.vuetifyjs.com/images/john.png"></v-img>
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
        <v-col cols="12" md="4" offset-md="1" class="d-flex align-center" >
          <v-btn block dark color="#F3B749">참여하기</v-btn>
        </v-col>
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
                {{data.startDay}}
              </div>
              <div class="mb-4">
                <v-icon class="mr-1">mdi-clock-outline</v-icon>
                {{data.startTime}}
              </div>
              <div class="mb-4">
                <v-icon class="mr-1">mdi-map-marker</v-icon>
                {{data.location}}
              </div>
              <div class="mb-4">
                <v-icon class="mr-1">mdi-account</v-icon>
                최대 {{data.member}}명 / {{data.age[0]}}세 ~ {{data.age[1]}}세까지
              </div>
              <div class="mb-4">
                <v-icon class="mr-1">mdi-gender-male-female</v-icon>
                {{data.gender}}
              </div>
              <div class="mb-4">
                <v-icon class="mr-1">mdi-currency-krw</v-icon>
                {{data.fee}}원
              </div>
            </v-card-text>
          </v-card>
          <div class="mb-12" id="mapview">
            <MapService></MapService>
          </div>
          <v-card class="excard">
            <div id="member">
              <v-card-title class="mb-3">
                모임 멤버 (1 / 10)
              </v-card-title>
              <v-chip pill class="ma-3">
                <v-avatar left>
                  <v-img src="https://cdn.vuetifyjs.com/images/john.png"></v-img>
                </v-avatar>
                {{data.username}}
              </v-chip>
            </div>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import MapService from '../components/MapService'

export default {
  name: 'Detail',
  components: {
    MapService
  },
  data () {
    return {
      data: {age: [0,0]},
      id: ''
    }
  },
  mounted () {
    this.id = this.$route.params.id
    this.get_detail();
},
  methods: {
    get_detail: function () {
      const api = "http://localhost:8000/boards/hobby"
      const api_url = api + '/' + this.id
      this.$http.get(api_url)
      .then(request => {
        this.data = request.data
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
