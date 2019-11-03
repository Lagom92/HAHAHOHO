<template>
  <div>
    <TopBanner></TopBanner>
    <v-container>
      <h1 class="text-center">모임 목록</h1>
      <div class="d-flex justify-end mx-3">
        <v-btn 
        fab 
        dark 
        icon 
        to="/list/createmeeting" 
        color="#74b4a0" 
        v-if="userId !== ''"
        > 
          <v-icon large>mdi-pencil-plus</v-icon>
        </v-btn>
      </div>
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
  },
  data () {
    return {
      userId: this.$store.state.user_id
    }
  },
}
</script>
