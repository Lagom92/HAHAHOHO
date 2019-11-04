<template>
  <div>
    <v-container>
      <v-row>
        <v-col cols="12" md="6" offset-md="3">
          <div>
            <h1 class="gamjaFont">모임 생성</h1>
          </div>
          <v-divider></v-divider>
          <v-file-input 
          accept="image/*" 
          label="모임 커버 사진" 
          v-model="img"
          :rules="imageRules"
          ></v-file-input>
          <v-form ref="form" v-model="valid">
            <v-text-field
            v-model="title"
            :counter="20"
            :rules="titleRules"
            label="글 제목"
            ></v-text-field>

            <v-textarea
            outlined
            v-model="contents"
            :rules="contentsRules"
            label="글 내용"
            ></v-textarea>

            <v-row>
              <v-col class="px-4">
                <v-range-slider
                v-model="ageRange"
                label="연령범위"
                :max="agemax"
                :min="agemin"
                hide-details
                thumb-label="always"
                step="10"
                class="align-center"
                color="#EE7785"
                track-color="#a7a7a2"
                ></v-range-slider>
              </v-col>
            </v-row>

            <v-row>
              <v-col cols="12" md="6">
                <v-select
                v-model="gender"
                :items="items"
                label="성별"
                required
                ></v-select>
              </v-col>
              <v-col cols="12" md="6">
                <v-text-field
                v-model="lineUp"
                min=2
                max=100
                label="최소 인원"
                :rules="lineUpRules"
                type="number"
                ></v-text-field>
              </v-col>
            </v-row>
            <!-- 모집 마감 날짜 -->
            <v-row>
              <v-col cols="12" md="6">
                <v-menu
                v-model="endingDate"
                :close-on-content-click="false"
                :nudge-right="40"
                transition="scale-transition"
                offset-y
                min-width="290px"
                >
                  <template v-slot:activator="{ on }">
                    <v-text-field
                    v-model="endDate"
                    label="모집 마감 날짜"
                    readonly
                    v-on="on"
                    ></v-text-field>
                  </template>
                  <v-date-picker
                  v-model="endDate"
                  @input="endingDate = false"
                  ></v-date-picker>
                </v-menu>
              </v-col>
            </v-row>
            <!-- 만나는 날짜, 시간 -->
            <v-row>
              <v-col cols="12" md="6">
                <v-menu
                v-model="meetingDate"
                :close-on-content-click="false"
                :nudge-right="40"
                transition="scale-transition"
                offset-y
                min-width="290px"
                >
                  <template v-slot:activator="{ on }">
                    <v-text-field
                    v-model="meetDate"
                    label="만나는 날짜"
                    readonly
                    v-on="on"
                    ></v-text-field>
                  </template>
                  <v-date-picker
                  v-model="meetDate"
                  @input="meetingDate = false"
                  ></v-date-picker>
                </v-menu>
              </v-col>
              <v-col cols="12" md="6">
                <v-menu
                ref="menu"
                v-model="meetingTime"
                :close-on-content-click="false"
                :nudge-right="40"
                :return-value.sync="meetTime"
                transition="scale-transition"
                offset-y
                max-width="290px"
                min-width="290px"
                >
                  <template v-slot:activator="{ on }">
                    <v-text-field
                    v-model="meetTime"
                    label="만나는 시간"
                    :rules="timeRules"
                    readonly
                    v-on="on"
                    ></v-text-field>
                  </template>
                  <v-time-picker
                  v-if="meetingTime"
                  v-model="meetTime"
                  full-width
                  @click:minute="$refs.menu.save(meetTime)"
                  ></v-time-picker>
                </v-menu>
              </v-col>
            </v-row>
            <div class="mb-5" id="mapsize">
              <!-- 지도 -->
              <MapService 
              :searchService="true"
              :address.sync="location"
              :height="'200px'"
              ></MapService>
            </div>
            <v-row>
              <v-col cols="12" md="3">
                <span>카테고리</span>
              </v-col>
              <v-col cols="12" md="9">
                <v-stepper v-model="e6" vertical>
                  <v-stepper-step :complete="e6 > 1" step="1" editable>
                    대분류 - {{this.sections}}
                  </v-stepper-step>

                  <v-stepper-content step="1">
                    <v-chip-group
                    active-class="deep-purple--text text--accent-4"
                    column
                    >
                      <v-chip
                      @click="selectClassification(k,v), e6 = 2"
                      filter
                      v-for="(v,k) in classification"
                      :key="(v,k)"
                      >
                        {{ k }}
                      </v-chip>
                    </v-chip-group>
                  </v-stepper-content>

                  <v-stepper-step :complete="e6 > 2" step="2">
                    소분류 - {{this.groups}}
                  </v-stepper-step>

                  <v-stepper-content step="2">
                    <v-chip-group
                    active-class="deep-purple--text text--accent-4"
                    column
                    >
                      <v-chip
                      @click="selectSubClassification(v)"
                      filter
                      v-for="v in this.selectSubClass"
                      :key="v"
                      >
                        {{ v }}
                      </v-chip>
                    </v-chip-group>
                    <v-btn color="primary" >선택완료</v-btn>
                  </v-stepper-content>
                </v-stepper>
              </v-col>
            </v-row>
            <v-row>
              <div class="ml-auto">
                <v-btn @click="onUpload()" text color="primary">
                  등록하기
                </v-btn>
              </div>
            </v-row>
          </v-form>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import MapService from '../components/MapService'
import axios from 'axios'

export default {
  name: 'createmeeting',
  components: {
    MapService
  },
  data () {
    return {
      title: '',
      contents: '',
      ageRange: [20, 40],
      gender: '상관없음',
      lineUp: '',
      endDate: new Date().toISOString().substr(0, 10),  // 모집 마감
      endTime: null,
      meetDate: new Date().toISOString().substr(0, 10), // 만나는 날짜
      meetTime: null,
      groups: '',
      valid: true,
      items: [
        '상관없음',
        '남성',
        '여성'
      ],
      classification: {
        '아웃도어': ['등산', '산책', '캠핑'],
        '스포츠': ['자전거', '배드민턴', '볼링'],
        '여행': ['국내여행', '해외여행'],
        '공연': ['영화', '전시회', '연극', '뮤지컬'],
        '음악': ['노래', '기타', '피아노'],
        '사교': ['봉사활동', '연애']
      },
      sections: '',
      selectSubClass: '',
      endingDate: false,  // 마감 날짜
      endingTime: false,
      meetingDate: false, // 만나는 날짜
      meetingTime: false,
      agemin: 10,
      agemax: 100,
      e6: 1,
      location: '광주 광역시',
      img: null,
      titleRules: [
        v => !!v || 'Title is required'
      ],
      contentsRules: [
        v => !!v || 'Contents is required'
      ],
      lineUpRules: [
        v => !!v || 'Min count is required'
      ],
      timeRules: [
        v => !!v || 'Time is required'
      ],
      imageRules: [
        v => !!v || 'Image is required'
      ],
    }
  },
  methods: {
    selectClassification (key, value) {
      this.sections = key
      this.selectSubClass = value
    },
    selectSubClassification (value) {
      this.groups = value
    },
    joinGroup: function (postId) {
      const baseUrl = this.$store.state.baseUrl
      const apiUrl = baseUrl + 'boards/participantCheck/' + postId + '/' + this.$store.state.user_id
      this.$http.post(apiUrl)
      .then(res => {})
      .catch(err => {
        console.log(err)
      })
    },
    onUpload () {
      const baseUrl = this.$store.state.baseUrl
      let form = new FormData()

      form.append('username', this.$store.state.user_name)
      form.append('user', this.$store.state.user_id)
      form.append('userimage', this.$store.state.user_image) //!!
      form.append('post', 1)  // 모임게시판 default 1
      form.append('postname', '모임 게시판')
      form.append('subclass', 1)
      form.append('subclassname', this.selectSubClass[0]) // !
      form.append('title', this.title)
      form.append('contents', this.contents)
      form.append('photo', this.img)
      form.append('gender', this.gender)
      form.append('minAge', this.ageRange[0])
      form.append('maxAge', this.ageRange[1])
      form.append('member', this.lineUp)
      form.append('location', this.location)

      form.append('startDay', this.meetDate)
      form.append('startTime', this.meetTime)

      form.append('endDay', this.endDate)
      form.append('endTime', this.meetTime) // !
 
      const apiUrl = baseUrl + 'boards/hobby'
      this.$http.post(apiUrl, form)
      .then(res => {
        this.joinGroup(res.data.id)
        
        this.$router.go(-1)
      })
      .catch(err => {
        console.log(err)
      })
      // axios.post(apiUrl, form, {
      //   headers: {
      //     'Authorization': 'Bearer ' + this.$store.state.user_jwt
      //   }
      // })
    },
  }
}
</script>

<style lang="stylus">

</style>
