<template>
  <div class="text-center">
    <v-card elevation="0" color="#00ff0000">
      <v-text-field
      label="Search"
      v-model="word" 
      append-outer-icon="mdi-magnify"
      single-line
      @keyup.enter="search()"
      ></v-text-field>      
    </v-card>
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  data () {
    return {
      word: ''
    }
  },
  methods: {
    search: function () {
      this.$store.commit('wordSave', this.word)
      var nowPosition = this.$router.history.current.name
      if (nowPosition == 'search') {
        window.location.reload()
      } else {
        this.$router.replace('search')
      }
    }
  }
}
</script>