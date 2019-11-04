<template>
    <v-container>
        <!-- 포인트 사용 내역 -->
        <v-col cols="12" md="10">
        <v-card class="pr-5" elevation="0" color="#fafafa">
            <v-card-title class="justify-center">
            Point 내역
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
              v-for="bill in this.bills"
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
          </v-card>
        </v-col>
    
        <!-- 카카오 페이 충전 내역 -->
        <v-col cols="12" md="10"> 
        <v-card class="pr-5" elevation="0" color="#fafafa">
            <v-card-title class="justify-center">
            Point 충전 내역
            <v-spacer></v-spacer>
            </v-card-title>
            <v-divider class="titleDiv"></v-divider>
            <v-row class="my-2" justify="center">
                <v-icon cols="1" small color="#EE7785"></v-icon>
                <v-col cols="3" class="subtitle-1 text-center">Money</v-col>
                <v-col cols="3" class="subtitle-1 text-center">contents</v-col>
                <v-col cols="3" class="subtitle-1 text-center">Date</v-col>
            </v-row>
            <v-divider class="titleDiv"></v-divider>
            <div
              v-for="kakaobill in this.kakaobills"
              :key="kakaobill.id"
            >
            <v-row class="my-2" justify="center">
                <v-icon cols="1" small color="#EE7785">mdi-water</v-icon>
                <v-col cols="3" class="subtitle-1 text-center">{{kakaobill.money}}</v-col>
                <v-col cols="3" class="subtitle-1 text-center">{{kakaobill.change}}</v-col>
                <v-col cols="3" class="subtitle-1 text-center">{{kakaobill.created_at}}</v-col>
            </v-row>
            <v-divider></v-divider>
            </div>
          </v-card>
        </v-col>
  </v-container>
</template>


<script>
export default {
  name: 'Bill',
  data () {
    return {
      bills: [],
      kakaobills: []
    }
  },
  mounted () {
    this.getBills()
    this.getKakaoBills()
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
      })
      .catch(err => {
        console.log(err)
      })
    },
    getKakaoBills: function () {
      const baseUrl = this.$store.state.baseUrl
      const apiUrl = baseUrl + 'accounts/bill/' + this.$store.state.user_id
      this.$http.get(apiUrl)
      .then(res => {
        for (let i of res.data){
            i.created_at = String(i.created_at).substring(0,10)
        }
        this.kakaobills = res.data
      })
      .catch(err => {
        console.log(err)
      })
    }
  }  
}

</script>