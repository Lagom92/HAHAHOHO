<template>
  <v-footer dark padless>
    <v-card flat tile width="100%" class="text-center" >
      <v-card-text>
        하하호호 즐거운 취미생활
      </v-card-text>
      <v-divider></v-divider>
      <v-card-text>
        2019 — <strong>SSAFY</strong>
      </v-card-text>
    </v-card>
  </v-footer>
</template>

<script>
export default {
  name: 'Footer',
  data () {
    return {
      icons: [
        'fab fa-facebook',
        'fab fa-twitter',
        'fab fa-google-plus',
        'fab fa-linkedin',
        'fab fa-instagram'
      ]
    }
  },
  components: {
    //
  }
}
</script>
