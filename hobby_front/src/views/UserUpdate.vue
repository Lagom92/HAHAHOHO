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
                <h3>이미지</h3>
              </v-col>
              <v-col cols="9">
                <v-img :src="img"></v-img>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="3">
                <h3>주소</h3>
              </v-col>
              <v-col cols="9">
                <v-dialog v-model="dialog" width="500">
                  <template v-slot:activator="{ on }">
                    <v-text-field v-model="result"></v-text-field>
                    <v-btn v-on="on">Click Me</v-btn>
                  </template>
                  <v-card>
                    <vue-daum-postcode @complete="result = $event, dialog=false, addResult()" />
                  </v-card>
                </v-dialog>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="3">
                <h3>선호카테고리</h3>
              </v-col>
              <v-col cols="9">
                <v-container class="py-0">
                  <v-row
                  align="center"
                  justify="start"
                  >
                    <v-col
                    v-for="(selection, i) in selections"
                    :key="selection.text"
                    class="shrink"
                    >
                      <v-chip
                      :disabled="loading"
                      close
                      @click:close="selected.splice(i, 1)"
                      >
                        <v-icon
                        left
                        v-text="selection.icon"
                        ></v-icon>
                        {{ selection.text }}
                      </v-chip>
                    </v-col>
                    <v-col v-if="!allSelected" cols="12">
                      <v-text-field
                      ref="search"
                      v-model="search"
                      full-width
                      hide-details
                      label="Search"
                      single-line
                      ></v-text-field>
                    </v-col>
                  </v-row>
                </v-container>
                <v-divider v-if="!allSelected"></v-divider>
                <v-list>
                  <template v-for="(item, i) in categories">
                    <v-list-item
                    v-if="!selected.includes(i)"
                    :key="i"
                    :disabled="loading"
                    @click="selected.push(i)"
                    >
                      <v-list-item-avatar>
                        <v-icon
                        :disabled="loading"
                        v-text="item.icon"
                        ></v-icon>
                      </v-list-item-avatar>
                      <v-list-item-title v-text="item.text"></v-list-item-title>
                    </v-list-item>
                  </template>
                </v-list>
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
      email: '',
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+\..+/.test(v) || 'E-mail must be valid'
      ],
      select: null,
      checkbox: false,
      items: [
        {
          text: '영화',
          icon: 'mdi-nature'
        },
        {
          text: '스포츠',
          icon: 'mdi-glass-wine'
        },
        {
          text: '등산',
          icon: 'mdi-calendar-range'
        },
        {
          text: '요리',
          icon: 'mdi-map-marker'
        },
        {
          text: '악기',
          icon: 'mdi-bike'
        }
      ],
      loading: false,
      search: '',
      selected: []
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
    next () {
      this.loading = true

      setTimeout(() => {
        this.search = ''
        this.selected = []
        this.loading = false
      }, 2000)
    },
    addResult () {
      let res = this.result.address
      this.result = res
    }
  },
  mounted() {
    let form = new FormData()
    this.$store.commit('idSave', 3)
    form.append('id', this.$store.state.user_id)
    this.$http.post(this.$store.state.baseUrl + 'accounts/userInfo', form).then(res =>{
      console.log(res)
      this.name = res.data.userName
      this.result = res.data.userAddress
      this.img = res.data.userImage
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
    }
  },
  watch: {
    selected () {
      this.search = ''
    }
  }
}
</script>
