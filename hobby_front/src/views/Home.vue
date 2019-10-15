<template>
  <div>
    <TopBanner></TopBanner>
    <v-container>
      <div class="intro">
        <h1>소개글</h1>
      </div>
      <v-row>
        <v-col cols="12" md="6">
          <v-card height="400px">모임목록</v-card>
        </v-col>
        <v-col cols="6" md="3">
          <v-card height="400px">공지사항</v-card>
        </v-col>
        <v-col cols="6" md="3">
          <v-card height="400px">자유게시판</v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import TopBanner from '../components/TopBanner'

export default {
  name: 'Home',
  components: {
    TopBanner
  }
}
</script>

<style>
  .intro {
    height: 30vh;
    background-color: #f2f2f2;
    margin-bottom: 50px;
  }
</style>