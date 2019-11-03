<template>
  <div>
    <v-row justify="center">
      <v-btn-toggle v-model="text" tile color="#EE7785" group>
        <v-btn value="new" @click="sortNew()">
          최신순
        </v-btn>
        <v-btn value="end" @click="sortEnd()">
          마감임박순
        </v-btn>
      </v-btn-toggle>
    </v-row>
    <v-layout wrap>
      <v-flex v-for="post in this.posts" :key="post.id" xs12 sm6 md4>
        <Meeting
        class='ma-3'
        :data="post"
        ></Meeting>
      </v-flex>
    </v-layout>
  </div>
</template>


<script>
import Meeting from '@/components/Meeting'

export default {
  name: 'MeetingList',
  data () {
    return {
      posts: [],
      text: ''
    }
  },
  components: {
    Meeting
  },
  mounted () {
    this.get_hobby();
  },
  methods: {
    get_hobby: function () {
      const api_url = "http://localhost:8000/boards/hobby"
      this.$http.get(api_url)
        .then(request => {
          this.posts = request.data 
        })
        .catch(err => {
          console.log(err)
        })
    },
    sortNew() {
      // var sortingField = 'created_at'
      this.posts.sort(function(a, b) {
        return a.created_at < b.created_at ? -1 : a.created_at < b.created_at ? 1 : 0
      })
    },
    sortEnd() {
      this.posts.sort(function(a, b) {
        return a.endDay < b.endDay ? -1 : a.endDay < b.endDay ? 1 : 0
      })
    }
  }  
}
</script>
