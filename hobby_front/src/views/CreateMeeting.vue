<template>
  <div>
    <v-container>
      <v-row>
        <v-col cols="12" md="6" offset-md="3">
          <div>
            <h1>모임 생성</h1>
          </div>
          <v-divider></v-divider>

          <v-file-input accept="image/*" label="모임 커버 사진"></v-file-input>

          <v-form ref="form" v-model="valid">
            <v-text-field
            v-model="title"
            :counter="10"
            label="글 제목"
            ></v-text-field>

            <v-textarea
            outlined
            v-model="contents"
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
                track-color="grey"
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
                label="최소 인원"
                type="number"
                ></v-text-field>
              </v-col>
            </v-row>

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
                    v-model="date"
                    label="만나는 날짜"
                    readonly
                    v-on="on"
                    ></v-text-field>
                  </template>
                  <v-date-picker
                  v-model="date"
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
                :return-value.sync="time"
                transition="scale-transition"
                offset-y
                max-width="290px"
                min-width="290px"
                >
                  <template v-slot:activator="{ on }">
                    <v-text-field
                    v-model="time"
                    label="만나는 시간"
                    readonly
                    v-on="on"
                    ></v-text-field>
                  </template>
                  <v-time-picker
                  v-if="meetingTime"
                  v-model="time"
                  full-width
                  @click:minute="$refs.menu.save(time)"
                  ></v-time-picker>
                </v-menu>
              </v-col>
            </v-row>
            <div class="mb-5" id="mapsize">
              <MapService :searchService="true"></MapService>
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
                <v-btn text color="primary">
                  임시저장
                </v-btn>

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
      content: '',
      ageRange: [20, 40],
      gender: null,
      lineUp: '',
      date: new Date().toISOString().substr(0, 10),
      time: null,
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
      meetingDate: false,
      meetingTime: false,
      agemin: 10,
      agemax: 100,
      e6: 1
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
    onUpload () {
      const baseUrl = this.$store.state.baseUrl
      let form = new FormData()

      form.append('title', this.title)
      form.append('contents', this.content)
      form.append('startDate', this.data + 'T' + this.time + ':00Z')
      form.append('gender', this.gender) // back 수정
      form.append('age', this.ageRange) // back 수정
      form.append('member', this.lineUp)
      form.append('location', null)
      form.append('fee', null)
      form.append('post', 1) // 1 : 모임 게시판
      form.append('group', this.groups)
      form.append('user', this.$store.state.user_id)

      axios.post(baseUrl + 'boards/hobby/', form, {
        headers: {
          'Authorization': 'Bearer ' + this.$store.state.user_jwt
        }
      })
    }
  }
}
</script>

<style lang="stylus">
#mapsize
  height 200px
  overflow auto
</style>
