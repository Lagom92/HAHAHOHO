<template>
  <div>
    <TopBanner></TopBanner>
    <v-container>
      <v-row>
        <h1 class="mx-auto">모임 목록</h1>
      </v-row>
      <v-row>
        <v-btn class="ml-auto pr-10 pb-10" text to="/list/createmeeting">
          <v-icon large>mdi-pencil-plus</v-icon>
        </v-btn>
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
