<template>
  <div>
    <v-container>
      <v-row>
        <v-col cols="12" md="8" offset-md="2">
          <div>
            <h1>정보수정</h1>
          </div>
          <v-divider class="ma-3"></v-divider>
          <v-img :src="img" height="250" width="250"></v-img>
          <v-file-input accept="image/*" label="프로필 사진"></v-file-input>
          <v-form ref="form" v-model="valid" >
            <v-text-field
            v-model="name"
            :counter="10"
            :rules="nameRules"
            label="닉네임"
            required
            ></v-text-field>
            <p class="mb-0">선호활동지역</p>
            <v-dialog v-model="dialog" width="500">
              <template v-slot:activator="{ on }">
                <v-text-field v-model="result"></v-text-field>
                <v-btn v-on="on">검색</v-btn>
              </template>
              <v-card>
                <vue-daum-postcode @complete="result = $event, dialog=false, addResult()" />
              </v-card>
            </v-dialog>
            <p class="mb-0">선호카테고리</p>
            <v-row>
              <v-col cols="12">
                <v-card class="mx-auto" >
                  <v-card-title class="title font-weight-regular justify-space-between">
                    <span>{{ currentTitle }}</span>
                    <v-avatar
                      color="primary lighten-2"
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
                            multiple
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
                          multiple
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
                      color="primary"
                      depressed
                      @click="nextstep()"
                    >
                      Next
                    </v-btn>
                  </v-card-actions>
                </v-card>
              </v-col>
            </v-row>
            <v-btn color="error" @click.stop="submit()">
              저장하기
            </v-btn>
          </v-form>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import { VueDaumPostcode } from "vue-daum-postcode"

export default {
  components: {
    VueDaumPostcode
  },
  data () {
    return {
      dialog:false,
      result:'',
      valid: true,
      img:'',
      name: '',
      nameRules: [
        v => !!v || 'Name is required',
        v => (v && v.length <= 10) || 'Name must be less than 10 characters'
      ],
      address: '',
      addressRules: [
        v => !!v || 'Address is required',
      ],
      cards: [
        { 
          title: '스포츠', 
          img: 'https://cdn.pixabay.com/photo/2015/01/26/22/40/child-613199_1280.jpg',
          sub: ['등산', '캠핑','볼링','축구','배구','배드민턴','자전거','탁구']
        },
        { 
          title: '여행', 
          img: 'https://cdn.pixabay.com/photo/2015/07/11/23/02/plane-841441_1280.jpg',
          sub: ['국내', '해외','낚시']  
        },
        { title: '공연/전시회', 
          img: 'https://cdn.pixabay.com/photo/2016/11/23/15/48/audience-1853662_1280.jpg',
          sub: ['영화', '뮤지컬','연극','콘서트']  
        },
        { title: '독서/인문학', 
          img: 'https://cdn.pixabay.com/photo/2016/01/19/17/53/books-1149959_1280.jpg',
          sub: ['책', '시사','글쓰기','인문학']
        },
        { title: '음악/악기', 
          img: 'https://cdn.pixabay.com/photo/2015/07/31/15/01/guitar-869217_1280.jpg',
          sub: ['노래', '기타','피아노','드럼']
        },
      ],
      selected: [],
      selected2: {},
      search: '',
      step: 1,
      CategoryList: {}
    }
  },
  methods: {
    validate () {
      if (this.$refs.form.validate()) {
        this.snackbar = true
      }
    },
    backstep() {
      this.step--
      this.CategoryList = {}
    },
    nextstep() {
      this.step++
      let data = {}
      for (var i of this.selected) {
        this.CategoryList[this.cards[i].title] = this.cards[i].sub
        data[this.cards[i].title] = []
        }
      this.selected2 = data
    },
    addResult() {
      let res = this.result.address
      this.result = res
    },
    submit() {
      let form = new FormData()
      let category = []
      for(let i of this.selected){
        for(let j of this.selected2[this.cards[i].title]){
          category.push(this.cards[i].sub[j])
        }
      }
      form.append('userLike', category)
      form.append('userAddress', this.result)
      form.append('userNickName', this.name)
      // 이미지 저장 후 요청보내기
      // form.append('userImage', this.img)
      console.log(form)
    }
  },
  mounted() {
    let form = new FormData()
    form.append('id', this.$store.state.user_id)
    let image
    this.$http.post(this.$store.state.baseUrl + 'accounts/userInfo', form).then(res =>{
      console.log(res)
      this.name = res.data.userName
      this.result = res.data.userAddress
      let counts = res.data.userImage.length
      image = res.data.userImage.substr(14, counts)
      this.img = 'https://'+image
    })
  },
  computed: {
    allSelected () {
      return this.selected.length === this.items.length
    },
    categories () {
      const search = this.search.toLowerCase()
      if (!search) return this.items

      return this.items.filter(item => {
        const text = item.text.toLowerCase()
        return text.indexOf(search) > -1
      })
    },
    selections () {
      const selections = []

      for (const selection of this.selected) {
        selections.push(this.items[selection])
      }
      return selections
    },
    currentTitle () {
        switch (this.step) {
          case 1: return '대분류'
          case 2: return '소분류'
        }
      }
  }
}
</script>
