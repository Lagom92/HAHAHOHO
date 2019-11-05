<template>
  <div>
    <v-container>
      <v-row>
        <v-col cols="12" md="2">
          <v-list-item>
            <v-list-item-content
            class="listItem"
            @click="currentpage = 0"
            >
              <span class="text-center">공지사항</span>
          </v-list-item-content>
          </v-list-item>
          <v-list-item>
            <v-list-item-content
            class="listItem"
            @click="currentpage = 1"
            >
              <span class="text-center">자유게시판</span>
            </v-list-item-content>
          </v-list-item>
          <v-list-item>
            <v-list-item-content
            class="listItem"
            @click="currentpage = 2"
            >
              <span class="text-center">FAQ</span>
            </v-list-item-content>
          </v-list-item>
        </v-col>
        <v-col cols="12" md="10">
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

<style lang="stylus">
.listItem
  cursor pointer
  font-weight bold
  position relative

.listItem:hover
  background #fafafa

.listItem:before, .listItem:after
  content ''
  position absolute
  bottom 0
  left 0
  height 2px
  width 0
  background #000
  transition 400ms ease all

.listItem:hover:before, .listItem:hover:after
  width 100%
  transition 800ms ease all
</style>