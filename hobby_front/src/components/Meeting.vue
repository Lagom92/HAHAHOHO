<template>
  <v-hover
  v-slot:default="{ hover }"
  >
    <v-card
    :elevation="hover ? 12 : 2"
    >
      <v-container class="pa-1">
        <router-link :to="'/list/detail/' + data.id" id="detailLink">
          <v-img
          :src= "data.photo"
          class="pa-2"
          height="250px"
          >
          </v-img>
        </router-link>
        <v-card-text class="plusbtn pt-6">
          <div class="mb-2" >
            <v-row class="px-3" align="center">
              <v-chip x-small color="#74b4a0" dark>{{data.subclass}}</v-chip>
              <v-chip
              v-if="data.new=='new'"
              class="ml-1"
              color="red"
              x-small
              dark
              >
                new
              </v-chip>
              <v-chip
              v-if="data.dead=='dead'"
              class="ml-1"
              color="blue"
              x-small
              dark
              >
                마감임박
              </v-chip>
              <v-spacer></v-spacer>
              <v-btn v-if="id" @click="selected()" color="#ff4e50" icon dark>
                <v-icon>
                  {{ active ? 'mdi-heart' : 'mdi-heart-outline' }}
                </v-icon>
              </v-btn>
            </v-row>
            <h3 class="meetingTitle title mb-2">{{data.title}}</h3>
          </div>
          <v-divider class="my-2"></v-divider>
          <v-row class="pl-3">
            <v-col class="pa-0">
              <v-icon small>mdi-clock-outline</v-icon>
              {{data.startDay}}
            </v-col>
            <v-col class="meetingLocation pa-0">
              <v-icon small>mdi-map-marker</v-icon>
              {{data.location}}
            </v-col>
          </v-row>
        </v-card-text>
      </v-container>
    </v-card>
  </v-hover>
</template>

<script>
export default {
  name: 'Meeting',
  data () {
    return {
      active: false,
      date: '',
      id: ''
    }
  },
  props: {
    data: {
    }
  },
  mounted () {
    this.id = this.$store.state.user_id
    if (this.$store.state.user_id) {
      this.$http.get(
        this.$store.state.baseUrl +
        'boards/cartList/' +
        this.$store.state.user_id
      ).then(res => {
        for (let i of res.data.post_id) {
          if (i === this.data.id) {
            this.active = true
          }
        }
      })
    }
  },
  methods: {
    selected () {
      let form = new FormData()
      form.append('post_id', this.data.id)
      this.$http.post(
        this.$store.state.baseUrl + 'boards/cart/' + this.$store.state.user_id,
        form
      ).then(res => {
        this.active = !this.active
      })
    }
  }
}
</script>

<style lang="stylus">
.meetingTitle
  text-overflow ellipsis
  white-space nowrap
  overflow hidden

.meetingLocation
  text-overflow ellipsis
  white-space nowrap
  overflow hidden

.plusbtn
  position relative

#detailLink
  text-decoration none
</style>
