<template>
  <div>
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
          console.log(request.data)
        })
        .catch(err => {
          console.log(err)
        })
    },
  }  
}
</script>
