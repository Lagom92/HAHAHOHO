<template>
  <v-container>
    <!-- 포인트 사용 내역 -->
    <v-col cols="12" md="10">
      <v-card class="pr-5" elevation="0" color="#fafafa">
        <v-card-title class="justify-center">
          Point 사용 내역
          <v-spacer></v-spacer>
        </v-card-title>
        <v-divider class="titleDiv"></v-divider>
        <v-row class="my-2" justify="center">
          <v-icon color="#EE7785" cols="1" small></v-icon>
          <v-col class="subtitle-1 text-truncate" cols="4">Title</v-col>
          <v-col class="subtitle-1 text-center" cols="2">Money</v-col>
          <v-col class="subtitle-1 text-center" cols="2">contents</v-col>
          <v-col class="subtitle-1 text-center" cols="2">Date</v-col>
        </v-row>
        <v-divider class="titleDiv"></v-divider>
        <div v-for="bill in paginatedData" :key="bill.id">
          <v-btn height="auto" :to="'/list/detail/' + bill.post_id" text block>
            <v-row class="my-2" justify="center">
              <v-icon cols="1" color="#EE7785" small>mdi-water</v-icon>
              <v-col class="subtitle-1 text-truncate" cols="4">
                {{bill.post_title}}
              </v-col>
              <v-col class="subtitle-1 text-center" cols="2">
                {{bill.money}}
              </v-col>
              <v-col class="subtitle-1 text-center" cols="2">
                {{bill.change}}
              </v-col>
              <v-col class="subtitle-1 text-center" cols="2">
                {{bill.created_at}}
              </v-col>
            </v-row>
          </v-btn>
          <v-divider></v-divider>
        </div>
        <div class="text-center my-5">
          <v-pagination :length="this.size" color="#74B4A0" v-model="pageNum">
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
      bills: [],
      pageNum: 1,
      size: null
    }
  },
  mounted () {
    this.getBills()
  },
  computed: {
    paginatedData () {
      const start = (this.pageNum - 1) * this.pageSize
      const end = start + this.pageSize
      return this.bills.slice(start, end)
    }
  },
  methods: {
    getBills: function () {
      const baseUrl = this.$store.state.base_url
      const apiUrl = baseUrl + 'boards/bill/' + this.$store.state.user_id
      this.$http.get(apiUrl)
        .then(res => {
          for (let i of res.data) {
            i.created_at = String(i.created_at).substring(0, 10)
          }
          this.bills = res.data
          let listLength = this.bills.length
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
