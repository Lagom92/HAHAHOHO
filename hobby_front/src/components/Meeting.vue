<template>
  <v-hover
  v-slot:default="{ hover }"
  >
    <v-card
    :elevation="hover ? 12 : 2"
    >
      <v-container class="pa-1">
        <v-item-group
        v-model="selected"
        multiple
        >
          <v-item v-slot:default="{ active, toggle }">
            <v-img
            :src= "data.photo"
            height="250px"
            class="text-right pa-2"
            >
              <v-btn icon dark color="#ff4e50" @click="toggle">
                <v-icon>
                  {{ active ? 'mdi-heart' : 'mdi-heart-outline' }}
                </v-icon>
              </v-btn>
            </v-img>
          </v-item>
          <v-card-text class="plusbtn pt-6">
            <v-btn
            absolute
            color="#EE7785"
            class="white--text"
            fab
            small
            right
            top
            :to="'/list/detail/' + data.id"
            >
              <v-icon>mdi-plus</v-icon>
            </v-btn>
            <div class="mb-2" >
              <v-chip x-small color="#74b4a0" dark>{{data.subclassname}}</v-chip>
              <h3 class="meetingTitle title mb-2">{{data.title}}</h3>
            </div>
            <v-divider class="my-2"></v-divider>
            <v-row class="pl-3">
              <v-col class="pa-0">
                <v-icon small>mdi-clock-outline</v-icon>{{data.startDay}}
              </v-col>
              <v-col class="meetingLocation pa-0">
                <v-icon small>mdi-map-marker</v-icon> {{data.location}}
              </v-col>
            </v-row>
          </v-card-text>
        </v-item-group>
      </v-container>
    </v-card>
  </v-hover>
</template>

<script>
export default {
  name: 'Meeting',
  data () {
    return {
      selected: [],
    }
  },
  props: {
    data: {}
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
</style>