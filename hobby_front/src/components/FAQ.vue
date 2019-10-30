<template>
  <div>
    <h1 class="mb-3">FAQ</h1>
    <v-divider id='topdivider'></v-divider>
    <v-expansion-panels focusable>
      <v-expansion-panel
        v-for="(post, i) in posts"
        :key="i"
      >
        <v-expansion-panel-header>{{post.title}}</v-expansion-panel-header>
        <v-expansion-panel-content class="pt-5">
          {{post.contents}} <br/><br>
          - {{post.name}} -
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
  </div>
</template>

<script>
export default {
  name: 'FAQ',
  data () {
    return {
      posts: []
    }
  },
  mounted () {
    this.getFaq();
  },
  methods: {
    getFaq: function () {
      const baseUrl = this.$store.state.baseUrl
      const apiUrl = baseUrl + 'boards/faq'
      this.$http.get(apiUrl)
        .then(res => {
          this.posts = res.data 
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>

<style lang="stylus">
#topdivider
  border-top-width 2px
  border-top-color #000
</style>
