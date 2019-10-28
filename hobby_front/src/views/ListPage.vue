<template>
  <div>
    <TopBanner></TopBanner>
    <v-container>
      <v-row>
        <h1>모임 목록</h1>
        <v-btn class="ml-auto" text to="/list/createmeeting">글쓰기</v-btn>
      </v-row>
      <v-layout>
        <v-flex>
          <MeetingList></MeetingList>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import TopBanner from '../components/TopBanner'
import MeetingList from '../components/MeetingList'

export default {
  name: 'ListPage',
  components: {
    MeetingList,
    TopBanner
  }
}
</script>
