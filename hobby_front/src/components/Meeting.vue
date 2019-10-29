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
            @click="toggle"
            >
              <v-btn icon dark color="#F3B749">
                <v-icon>
                  {{ active ? 'mdi-heart' : 'mdi-heart-outline' }}
                </v-icon>
              </v-btn>
            </v-img>
          </v-item>
          <v-card-text class="pt-6" style="position: relative;">
            <v-btn
            absolute
            color="#F3B749"
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
              <v-chip small color="#9AB878" dark>{{data.subclassname}}</v-chip>
            </div>
            <h3 class="headline mb-2" color="#F3B749">{{data.title}}</h3>
            <v-divider class="my-3"></v-divider>
            <v-row class="pl-3">
              <v-col class="pa-0">
                <v-icon small>mdi-clock-outline</v-icon> {{data.startDay}}
              </v-col>
              <v-col class="pa-0">
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