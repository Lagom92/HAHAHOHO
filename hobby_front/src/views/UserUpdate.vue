<template>
  <div>
    <v-container>
      <v-row>
        <v-col cols="6" offset="3">
          <div>
            <h1>정보수정</h1>
          </div>
          <v-form
          ref="form"
          v-model="valid"
          lazy-validation
          >
            <v-row>
              <v-col cols="3">
                <h3>이름</h3>
              </v-col>
              <v-col cols="9">
                <v-text-field
                v-model="name"
                :counter="10"
                :rules="nameRules"
                label="Name"
                required
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="3">
                <h3>주소</h3>
              </v-col>
              <v-col cols="9">
                <v-text-field
                v-model="address"
                label="Address"
                required
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="3">
                <h3>선호카테고리</h3>
              </v-col>
              <v-col cols="9">
                <v-card
                  class="mx-auto"
                  max-width="500"
                >
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
                        max-width="400"
                        class="mx-auto"
                      >
                        <v-container class="pa-1">
                          <v-item-group
                            v-model="selected"
                            multiple
                          >
                            <v-row>
                              <v-col
                                v-for="(card, i) in cards"
                                :key="i"
                                cols="12"
                                md="6"
                              >
                                <v-card>
                                  <v-item v-slot:default="{ active, toggle }">
                                    <v-img
                                      :src="card.img"
                                      class="white--text align-end"
                                      height="150"
                                      gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                                      @click="toggle"
                                    >
                                      <v-card-title v-text="card.title"></v-card-title>
                                      <v-btn icon dark >
                                        <v-icon>
                                          {{ active ? 'mdi-heart' : 'mdi-heart-outline' }}
                                        </v-icon>
                                      </v-btn>
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
                        v-for="category in categoryList"
                        :key="category">
                        <h3 class="title mb-2">{{category}}</h3>

                        <v-chip-group
                          column
                          multiple
                        >
                          <v-chip 
                            filter 
                            outlined
                            v-for="sub in subCategoryList"
                            :key="sub"
                          >
                            {{sub}}
                          </v-chip>
                        </v-chip-group>
                      </v-card-text>
                    </v-window-item>

                    <v-window-item :value="3">
                      <div class="pa-4 text-center">
                        <v-img
                          class="mb-4"
                          contain
                          height="128"
                          src="https://cdn.vuetifyjs.com/images/logos/v.svg"
                        ></v-img>
                        <h3 class="title font-weight-light mb-2">Welcome to Vuetify</h3>
                        <span class="caption grey--text">Thanks for signing up!</span>
                      </div>
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
                      :disabled="step === 3"
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
            <v-checkbox
            v-model="checkbox"
            :rules="[v => !!v || 'You must agree to continue!']"
            label="Do you agree?"
            required
            ></v-checkbox>
            <v-btn
            :disabled="!valid"
            color="success"
            class="mr-4"
            @click="validate"
            >
              수정
            </v-btn>
            <v-btn
            color="error"
            class="mr-4"
            @click="reset"
            >
              초기화
            </v-btn>
          </v-form>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  data () {
    return {
      valid: true,
      name: '',
      nameRules: [
        v => !!v || 'Name is required',
        v => (v && v.length <= 10) || 'Name must be less than 10 characters'
      ],
      address: '',
      select: null,
      checkbox: false,
      cards: [
        { 
          title: '스포츠', 
          img: 'https://cdn.pixabay.com/photo/2015/01/26/22/40/child-613199_1280.jpg',
          sub: ['등산', '캠핑','해외여행','국내여행']
        },
        { 
          title: '여행', 
          img: 'https://cdn.pixabay.com/photo/2015/07/11/23/02/plane-841441_1280.jpg',
          sub: ['1', '2','3','4']  
        },
        { title: '공연/전시회', 
          img: 'https://cdn.pixabay.com/photo/2016/11/23/15/48/audience-1853662_1280.jpg',
          sub: ['11', '22','33','44']  
        },
        { title: '독서/인문학', 
          img: 'https://cdn.pixabay.com/photo/2016/01/19/17/53/books-1149959_1280.jpg',
          sub: ['12', '23','34','45']
        },
      ],
      selected: [],
      loading: false,
      search: '',
      step: 1,
      categoryList: [],
      subCategoryList: []
    }
  },
  methods: {
    validate () {
      if (this.$refs.form.validate()) {
        this.snackbar = true
      }
    },
    reset () {
      this.$refs.form.reset()
    },
    backstep() {
      this.step--
      this.categoryList = []
      this.subCategoryList = []
    },
    nextstep() {
      this.step++
      for (var i of this.selected) {
        this.categoryList.push(this.cards[i].title)
        for (var j of this.cards[i].sub) {
          this.subCategoryList.push(j)
        }
      }      
    }
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
          default: return 'Account created'
        }
      }
  },
  watch: {
    selected () {
      this.search = ''
    }
  }
}
</script>
