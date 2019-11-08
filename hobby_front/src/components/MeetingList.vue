<template>
  <div>
    <v-row>
      <v-btn-toggle v-model="text" color="#EE7785" tile group>
        <v-btn @click="sortNew()" value="new" class="nanumFont">
          최신순
        </v-btn>
        <v-btn @click="sortEnd()" value="end" class="nanumFont">
          마감임박순
        </v-btn>
      </v-btn-toggle>
    </v-row>
    <v-layout wrap>
      <v-flex v-for="post in paginatedData" :key="post.id" xs12 sm6 md4>
        <Meeting
        class='ma-3'
        :data="post"
        ></Meeting>
      </v-flex>
    </v-layout>
    <div class="text-center my-5">
        <v-pagination :length="this.size" v-model="pageNum" color="#74B4A0">
        </v-pagination>
    </div>
  </div>
</template>

<script>
import Meeting from '@/components/Meeting'

export default {
  name: 'MeetingList',
  props: {
    pageSize: { type: Number, required: false, default: 6 }
  },
  data () {
    return {
      posts: [],
      text: '',
      pageNum: 1,
      size: null
    }
  },
  components: {
    Meeting
  },
  mounted () {
    this.get_hobby()
  },
  computed: {
    paginatedData () {
      const start = (this.pageNum - 1) * this.pageSize
      const end = start + this.pageSize
      return this.posts.slice(start, end)
    }
  },
  methods: {
    get_hobby: function () {
      const baseUrl = this.$store.state.base_url
      const apiUrl = baseUrl + 'boards/hobby'
      this.$http.get(apiUrl)
        .then(res => {
          this.posts = res.data
          let listLength = this.posts.length
          let listSize = this.pageSize
          let page = Math.floor((listLength - 1) / listSize) + 1
          this.size = page
          for (let i of res.data) {
            let timeMins = Date.now()
            let createTime = new Date(i.created_at).getTime()
            let deadTime = new Date(i.endDay).getTime()
            let subToCreate = Math.floor(timeMins - createTime) / 1000
            let subToEnd = Math.floor(timeMins - deadTime) / 1000
            if (Math.floor(subToCreate / 86400) < 1) {
              i.new = 'new'
            } else {
              i.new = null
            }
            if (subToEnd > 0 && subToEnd < 86400) {
              i.dead = 'dead'
            } else {
              i.dead = null
            }
          }
          this.posts = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    sortNew () {
      this.posts.sort(function (a, b) {
        return a.created_at > b.created_at ? -1 : a.created_at < b.created_at ? 1 : 0
      })
    },
    sortEnd () {
      this.posts.sort(function (a, b) {
        return a.endDay < b.endDay ? -1 : a.endDay > b.endDay ? 1 : 0
      })
    }
  }
}
</script>
