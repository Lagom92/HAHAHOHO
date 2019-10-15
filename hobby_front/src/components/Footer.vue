<template>
  <v-footer dark padless height="auto" absolute>
    <v-card flat tile width="100%" class="indigo lighten-1 text-center" >
      <v-card-text class="white--text">
        하하호호 즐거운 취미생활
      </v-card-text>

      <v-divider></v-divider>

      <v-card-text class="white--text">
        2019 — <strong>SSAFY</strong>
      </v-card-text>
    </v-card>
  </v-footer>
</template>

<script>
  export default {
    name: "Footer",
    data: () => ({
      icons: [
        'fab fa-facebook',
        'fab fa-twitter',
        'fab fa-google-plus',
        'fab fa-linkedin',
        'fab fa-instagram',
      ],
    }),
  }
</script>