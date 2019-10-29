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
  components: {
    Header,
    Footer
  },
  store
}
</script>
