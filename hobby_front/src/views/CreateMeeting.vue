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
          chips 
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
              <v-col cols="12">
                <v-card class="mx-auto" >
                  <v-card-title class="title font-weight-regular justify-space-between">
                    <span>{{ currentTitle }}</span>
                    <v-avatar
                      color="#ee7785"
                      class="subheading white--text"
                      size="24"
                      v-text="step"
                    ></v-avatar>
                  </v-card-title>

                  <v-window v-model="step">
                    <v-window-item :value="1">
                      <v-card
                        elevation="0"
                        class="mx-auto"
                      >
                        <v-container class="px-5">
                          <v-item-group
                            v-model="selected"
                          >
                            <v-row>
                              <v-col
                                v-for="(card, i) in cards"
                                :key="i"
                                cols="12"
                                md="4"
                              >
                                <v-card>
                                  <v-item v-slot:default="{ active, toggle }">
                                    <v-img
                                      :src="card.img"
                                      class="white--text align-center"
                                      height="150"
                                      gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                                      @click="toggle"
                                    >
                                      <v-btn icon dark class="mb-10">
                                        <v-icon>
                                          {{ active ? 'mdi-heart' : 'mdi-heart-outline' }}
                                        </v-icon>
                                      </v-btn>
                                      <v-card-title v-text="card.title" class="justify-center"></v-card-title>
                                    </v-img>
                                  </v-item>
                                </v-card>
                              </v-col>
                            </v-row>
                          </v-item-group>
                        </v-container>
                      </v-card>
                    </v-window-item>

                    <v-window-item :value="2">
                      <v-card-text 
                        v-for="(sub,category) in CategoryList"
                        :key="category">
                        <h3 class="title mb-2">{{category}}</h3>

                        <v-chip-group
                          column
                          v-model="selected2[category]"
                        >
                          <v-chip 
                            filter 
                            outlined
                            v-for="s in sub"
                            :key="s"
                          >
                            {{s}}
                          </v-chip>
                        </v-chip-group>
                      </v-card-text>
                    </v-window-item>
                  </v-window>

                  <v-divider></v-divider>

                  <v-card-actions>
                    <v-btn
                      :disabled="step === 1"
                      text
                      @click="backstep()"
                    >
                      Back
                    </v-btn>
                    <v-spacer></v-spacer>
                    <v-btn
                      :disabled="step === 2"
                      depressed
                      text
                      @click="nextstep()"
                    >
                      Next
                    </v-btn>
                  </v-card-actions>
                </v-card>
              </v-col>
            </v-row>
            <v-row>
              <div class="ml-auto">
                <v-btn @click="onUpload()" dark color="#74b4a0">
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
      cards: [
        { 
          title: '스포츠', 
          img: 'https://cdn.pixabay.com/photo/2015/01/26/22/40/child-613199_1280.jpg',
          sub: ['축구', '볼링','자전거','낚시','야구','농구','당구','탁구', '클라이밍', '헬스', '요가/필라테스', '스케이트', '보드', '골프', '배드민턴', '댄스', '기타']
        },
        { 
          title: '여행', 
          img: 'https://cdn.pixabay.com/photo/2015/07/11/23/02/plane-841441_1280.jpg',
          sub: ['캠핑', '글램핑','국내여행', '해외여행', '드라이브', '라이딩', '출사', '천체관측', '기타']  
        },
        { title: '문화/공연/축제', 
          img: 'https://cdn.pixabay.com/photo/2016/11/23/15/48/audience-1853662_1280.jpg',
          sub: ['영화 관람', '뮤지컬 관람','전시회 관람','연극 관람', '축제', '스포츠 관람', '코스프레', '버스킹', '기타']  
        },
        { title: '창작', 
          img: 'https://cdn.pixabay.com/photo/2016/01/19/17/53/books-1149959_1280.jpg',
          sub: ['캘리그라피', '플라워아트','뜨개질','캔들/디퓨저/석고', '비누/화장품', '가죽공예', '소품공예', '프라모델', '그림그리기', '연주', '작곡', '글쓰기', '프로그래밍', '기타']
        },
        { title: '사교/인맥', 
          img: 'https://cdn.pixabay.com/photo/2015/07/31/15/01/guitar-869217_1280.jpg',
          sub: ['커피', '독서','술','맛집', '반려동물', '육아', '보드게임', '온라인 게임', '콘솔게임', '타로', '봉사활동', '증권투자', '기타']
        },
        {
          title: '기타',
          img: 'https://cdn.pixabay.com/photo/2015/03/20/17/45/etc-682613_1280.jpg',
          sub: ['기타']
        }
      ],
      step: 1,
      CategoryList: {},
      selected: [],
      selected2: {},
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
  computed: {
    currentTitle () {
        switch (this.step) {
          case 1: return '대분류'
          case 2: return '소분류'
        }
    },
  },
  methods: {
    backstep() {
      this.step--
      this.CategoryList = {}
    },
    nextstep() {
      this.step++
      let data = {}
      this.CategoryList[this.cards[this.selected].title] = this.cards[this.selected].sub
      data[this.cards[this.selected].title] = []
      this.selected2 = data
    },
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
      let subclass = this.selected2[this.cards[this.selected].title]
      let subclassname = this.cards[this.selected].sub[subclass]

      form.append('username', this.$store.state.user_name)
      form.append('user', this.$store.state.user_id)
      form.append('userimage', this.$store.state.user_image) //!!
      form.append('post', 1)  // 모임게시판 default 1
      form.append('postname', '모임 게시판')
      form.append('subclass', subclassname) // !
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
    },
  }
}
</script>

<style lang="stylus">

</style>
