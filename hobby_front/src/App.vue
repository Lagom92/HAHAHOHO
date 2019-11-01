<template>
  <v-app>
    <Header></Header>
    <v-content>
      <router-view></router-view>
    </v-content>
    <Footer></Footer>
  </v-app>
</template>

<script>
import Header from '@/components/Header'
import Footer from '@/components/Footer'
import store from './store'

export default {
  name: 'App',
  data () {
    return {
      //
    }
  },
  mounted() {
    Kakao.init('b9b23d9b337a41dca3e1632a4677e0af')
  },
  components: {
    Header,
    Footer
  },
  store
}
</script>
