import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import List from './views/ListPage.vue'
import Board from './views/BoardPage.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/list',
      name: 'list',
      component: List
    },
    {
      path: '/board',
      name: 'board',
      component: Board
    }
  ]
})
