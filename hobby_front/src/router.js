import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import List from './views/ListPage.vue'
import Board from './views/BoardPage.vue'
import User from './views/UserPage.vue'
import UserUpdate from './views/UserUpdate.vue'
import Detail from './views/Detail.vue'
import NaverLoginCallBack from './views/NaverLoginCallBack.vue'
import CreateMeeting from './views/CreateMeeting.vue'
import About from './views/About.vue'
import CreateFreeboard from './views/CreateFreeboard.vue'
import NoticeDetail from './components/NoticeDetail.vue'
import FreeBoardDetail from './components/FreeBoardDetail.vue'

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
      path: '/list/detail/:id',
      name: 'detail',
      component: Detail // 임시로 페이지 확인을 위해 만들어놓은 라우터, 나중에 수정해야함
    },
    {
      path: '/notice/:id',
      name: 'notice',
      component: NoticeDetail 
    },
    {
      path: '/free/:id',
      name: 'free',
      component: FreeBoardDetail 
    },
    {
      path: '/login',
      name: 'naverLoginCallBack',
      component: NaverLoginCallBack
    },
    {
      path: '/list/createmeeting',
      name: 'createmeeting',
      component: CreateMeeting
    },
    {
      path: '/about',
      name: 'about',
      component: About
    },
    {
      path: '/createfreeboard',
      name: 'createfreeboard',
      component: CreateFreeboard
    }
  ],
  scrollBehavior (to, from, savedPosition) {
    return { x: 0, y: 0 }
  }
})
