<template>
  <div>
    <v-container>
      <v-row>
        <v-col cols="2">
          <v-list-item>
            <v-list-item-content
            @click="currentpage = 0"
            >
              공지사항
          </v-list-item-content>
          </v-list-item>
          <v-list-item>
            <v-list-item-content
            @click="currentpage = 1"
            >
              자유게시판
            </v-list-item-content>
          </v-list-item>
          <v-list-item>
            <v-list-item-content
            @click="currentpage = 2"
            >
              FAQ
            </v-list-item-content>
          </v-list-item>
        </v-col>
        <v-col cols="10">
          <Notice v-if="this.currentpage == 0"></Notice>
          <FreeBoard v-else-if="this.currentpage == 1"></FreeBoard>
          <FAQ v-else-if="this.currentpage == 2"></FAQ>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import Notice from '../components/Notice'
import FreeBoard from '../components/FreeBoard'
import FAQ from '../components/FAQ'

export default {
  name: 'BoardPage',
  components: {
    Notice,
    FreeBoard,
    FAQ
  },
  props: {
    propsPage: { type: Number, default: 0}
  },
  data () {
    return {
      currentpage: this.propsPage 
    }
  }
}
</script>
