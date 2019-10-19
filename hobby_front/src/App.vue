<template>
  <v-app>
    <v-content>
      <Header></Header>
      <router-view></router-view>
      <Payment></Payment>
      <Footer></Footer>
    </v-content>
  </v-app>
</template>

<script>
import Header from '@/components/Header'
import Footer from '@/components/Footer'
import Payment from '@/components/Payment'

export default {
  name: 'App',
  data: () => ({
    //
  }),
  components: {
    Header,
    Footer,
    Payment
  }
}
</script>
