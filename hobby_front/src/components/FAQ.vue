<template>
  <div>
    <h1 class="mb-3 malarenFont">FAQ</h1>
    <v-divider id='topdivider'></v-divider>
    <v-expansion-panels focusable>
      <v-expansion-panel
        v-for="(post, i) in posts"
        :key="i"
      >
        <v-expansion-panel-header>{{post.title}}</v-expansion-panel-header>
        <v-expansion-panel-content class="pt-5">
          <xmp>{{post.contents}}</xmp>
          <br/><br/>
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
    this.getFaq()
  },
  methods: {
    getFaq: function () {
      const baseUrl = this.$store.state.base_url
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
xmp
  white-space pre-wrap
  word-wrap break-word

#topdivider
  border-top-width 2px
  border-top-color #000

.malarenFont
  font-family 'Gaegu', cursive
</style>
