<template>
  <v-container>
    <!-- 카카오 페이 충전 내역 -->
    <v-col cols="12" md="10">
      <v-card class="pr-5" elevation="0" color="#fafafa">
        <v-card-title class="justify-center">
          Point 충전 내역
          <v-spacer></v-spacer>
        </v-card-title>
        <v-divider class="titleDiv"></v-divider>
        <v-row class="my-2" justify="center">
          <v-icon cols="1" color="#EE7785" small></v-icon>
          <v-col class="subtitle-1 text-center" cols="3">Money</v-col>
          <v-col class="subtitle-1 text-center" cols="3">contents</v-col>
          <v-col class="subtitle-1 text-center" cols="3">Date</v-col>
        </v-row>
        <v-divider class="titleDiv"></v-divider>
        <div
        v-for="kakaobill in paginatedData"
        :key="kakaobill.id"
        >
          <v-row class="my-2" justify="center">
            <v-icon cols="1" color="#EE7785" small>mdi-water</v-icon>
            <v-col class="subtitle-1 text-center" cols="3">
              {{kakaobill.money}}
            </v-col>
            <v-col class="subtitle-1 text-center" cols="3">
              {{kakaobill.change}}
            </v-col>
            <v-col class="subtitle-1 text-center" cols="3">
              {{kakaobill.created_at}}
            </v-col>
          </v-row>
          <v-divider></v-divider>
        </div>
        <div class="text-center my-5">
          <v-pagination :length="this.size" v-model="pageNum" color="#74B4A0">
          </v-pagination>
        </div>
      </v-card>
    </v-col>
  </v-container>
</template>

<script>
export default {
  name: 'Bill',
  props: {
    pageSize: { type: Number, required: false, default: 3 }
  },
  data () {
    return {
      kakaobills: [],
      pageNum: 1,
      size: null
    }
  },
  mounted () {
    this.getKakaoBills()
  },
  computed: {
    paginatedData () {
      const start = (this.pageNum - 1) * this.pageSize
      const end = start + this.pageSize
      return this.kakaobills.slice(start, end)
    }
  },
  methods: {
    getKakaoBills () {
      const baseUrl = this.$store.state.base_url
      const apiUrl = baseUrl + 'accounts/bill/' + this.$store.state.user_id
      this.$http.get(apiUrl)
        .then(res => {
          for (let i of res.data) {
            i.created_at = String(i.created_at).substring(0, 10)
          }
          this.kakaobills = res.data

          let listLength = this.kakaobills.length
          let listSize = this.pageSize
          let page = Math.floor((listLength - 1) / listSize) + 1
          this.size = page
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}

</script>
