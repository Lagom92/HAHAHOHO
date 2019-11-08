<template>
  <div>
    <TopBanner></TopBanner>
    <v-container>
      <h1 class="text-center gamjaFont" id="titlesize">모임</h1>
      <div class="d-flex justify-end mx-3">
        <v-btn
        v-if="userId !== ''"
        @click="move()"
        color="#74b4a0"
        fab
        dark
        icon
        >
          <v-icon large>mdi-pencil-plus</v-icon>
        </v-btn>
      </div>
      <v-snackbar
      v-model="snackbar"
      :vertical="vertical"
      color="success"
      >
        {{ ment }}
        <div class="ml-auto">
          <v-btn
          class="ml-auto"
          @click="snackbar = false, moveTo()"
          color="white"
          text
          >
            go
          </v-btn>
          <v-btn
          class="ml-auto"
          color="white"
          text
          @click="snackbar = false"
          >
            Close
          </v-btn>
        </div>
      </v-snackbar>
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
      userId: this.$store.state.user_id,
      snackbar: false,
      ment: '유저정보 수정을 위해 이동하시겠습니까?',
      vertical: true
    }
  },
  methods: {
    move () {
      if (this.$store.state.user_grade === 1) {
        alert('글 작성을 위해서 유저정보를 수정해 주세요')
        this.snackbar = true
      } else {
        this.$router.push({ name: 'createmeeting' })
      }
    },
    moveTo () {
      this.$router.push({ name: 'user' })
    }
  }
}
</script>

<style lang="stylus">
#titlesize
  font-size 40px
</style>
