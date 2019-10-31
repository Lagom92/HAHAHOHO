<template>
  <div>
    <v-card elevation="0" color="#00ff0000">
      <!-- <v-text-field
      label="Search"
      append-outer-icon="mdi-magnify"
      single-line
      
      ></v-text-field> -->
      검색: 
      <input 
        v-model="word" 
        placeholder="여기를 수정해보세요" 
        @keyup.enter="search()"
      >

    </v-card>
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  data () {
    return {
      posts: [],
      word: ''
    }
  },
  methods: {
    search: function () {
      const baseUrl = this.$store.state.baseUrl
      console.log(this.word)
      const apiUrl = baseUrl + 'boards/hobby?q=' + this.word
      this.$http.get(apiUrl)
        .then(res => {
          console.log(res)
          this.posts = res.data
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>
