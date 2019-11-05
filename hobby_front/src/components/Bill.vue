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
                <v-icon cols="1" small color="#EE7785"></v-icon>
                <v-col cols="4" class="subtitle-1 text-truncate">Title</v-col>
                <v-col cols="2" class="subtitle-1 text-center">Money</v-col>
                <v-col cols="2" class="subtitle-1 text-center">contents</v-col>
                <v-col cols="2" class="subtitle-1 text-center">Date</v-col>
            </v-row>
            <v-divider class="titleDiv"></v-divider>
            <div
              v-for="bill in paginatedData"
              :key="bill.id"
            >
            <v-btn
                text
                block
                height="auto"
                :to="'/list/detail/' + bill.post_id"
              >
            <v-row class="my-2" justify="center">
                <v-icon cols="1" small color="#EE7785">mdi-water</v-icon>
                <v-col cols="4" class="subtitle-1 text-truncate">
                {{bill.post_title}}
                </v-col>
                <v-col cols="2" class="subtitle-1 text-center">{{bill.money}}</v-col>
                <v-col cols="2" class="subtitle-1 text-center">{{bill.change}}</v-col>
                <v-col cols="2" class="subtitle-1 text-center">{{bill.created_at}}</v-col>
            </v-row>
            </v-btn>
            <v-divider></v-divider>
            </div>
            <div class="text-center my-5">
                <v-pagination v-model="pageNum" :length="this.size" color="#74B4A0"></v-pagination>
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
  computed: {
    paginatedData() {
      const start = (this.pageNum - 1) * this.pageSize,
            end = start + this.pageSize
      return this.bills.slice(start, end)
    }
  },
  mounted () {
    this.getBills()
  },
  methods: {
    getBills: function () {
      const baseUrl = this.$store.state.baseUrl
      const apiUrl = baseUrl + 'boards/bill/' + this.$store.state.user_id
      this.$http.get(apiUrl)
      .then(res => {
        for (let i of res.data){
            i.created_at = String(i.created_at).substring(0,10)
        }
        this.bills = res.data
        let listLength = this.bills.length,
          listSize = this.pageSize,
          page = Math.floor((listLength - 1) / listSize) + 1
          this.size = page
      })
      .catch(err => {
        console.log(err)
      })
    },
  }  
}

</script>