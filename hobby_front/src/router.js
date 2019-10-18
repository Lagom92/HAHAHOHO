import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import List from './views/ListPage.vue'
import Board from './views/BoardPage.vue'
import User from './views/UserPage.vue'
import UserUpdate from './views/UserUpdate.vue'
import Detail from './views/Detail.vue'

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
    },
    {
      path: '/user',
      name: 'user',
      component: User
    },
    {
      path: '/userupdate',
      name: 'userupdate',
      component: UserUpdate
    },
    {
      path: '/list/detail',
      name: 'detail',
      component: Detail // 임시로 페이지 확인을 위해 만들어놓은 라우터, 나중에 수정해야함
    }
  ]
})
