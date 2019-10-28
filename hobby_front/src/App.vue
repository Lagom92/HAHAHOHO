<template>
  <v-app>
    <v-content>
      <Header></Header>
      <router-view></router-view>
      <Footer></Footer>
    </v-content>
  </v-app>
</template>

<script>
import Header from '@/components/Header'
import Footer from '@/components/Footer'
import store from "./store";

export default {
  name: 'App',
  data: () => ({
    //
  }),
  components: {
    Header,
    Footer
  },
  store,
}
</script>
