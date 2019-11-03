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
      const baseUrl = this.$store.state.baseUrl
      const apiUrl = baseUrl + 'boards/hobby'
      this.$http.get(apiUrl)
        .then(res => {
          this.posts = res.data 
        })
        .catch(err => {
          console.log(err)
        })
    },
  }  
}
</script>
