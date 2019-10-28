import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user_id: '',
    user_jwt: '',
    // baseUrl: "http://54.180.148.99:8000/"
    baseUrl: 'http://localhost:8000/'
  },
  mutations: {
    idSave (state, id) {
      state.user_id = id
    },
    jwtSave (state, jwt) {
      state.user_jwt = jwt
    }
  },
  actions: {

  }
})
