<template>
  <div class="topBanner pt-5 px-5 pb-12">
    <v-container>
      <v-row class="mb-7" align="center">
        <v-col class="d-flex justify-center" cols="12" md="8">
          <v-img src="../assets/hahahoho.png" max-width="75%"></v-img>
        </v-col>
        <v-col class="d-none d-md-flex" cols="12" sm="4">
          <span class="bannerText mb-3 dohyeonFont">
            다같이<br/>
            놀아요<br/>
            룰루랄라
          </span>
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
  height auto
  background radial-gradient(circle, #fafafa, #e1ffe9)
  margin-bottom 50px

.bannerText
  color #EE7785

.dohyeonFont
  font-family 'Do Hyeon', sans-serif
  font-size 50px
</style>
