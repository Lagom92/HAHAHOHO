<template>
  <div class="topBanner">
    <v-container>
      <v-row align="center" class="mb-10">
        <v-col cols="12" md="8" class="d-flex justify-center">
          <v-img id="hahahoho" src="../assets/hahahoho.png" max-width="55%"></v-img>
        </v-col>
        <v-col cols="12" md="4">
          <p class="bannerText display-1 font-weight-bold mb-2 d-none d-md-flex">취미모임</p>
          <p class="bannerText display-1 font-weight-bold mb-2 d-none d-md-flex">다같이 놀아요</p>
          <p class="bannerText display-1 font-weight-bold mb-0 d-none d-md-flex">룰루랄라</p>
        </v-col>
      </v-row>
      <SearchBar></SearchBar>
    </v-container>
  </div>
</template>

<script>
import SearchBar from './SearchBar'

export default {
  name: 'TopBanner',
  components: {
    SearchBar
  }
}
</script>

<style lang="stylus">
.topBanner
  position relative
  height 50vh
  background-color #f2f2f2
  margin-bottom 50px

.bannerText
  color #EE7785
</style>