import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user_id: '',
    user_jwt: ''
  },
  mutations: {
    idSave(state, id) {
      state.user_id = id
    },
    jwtSave(state, jwt) {
      state.user_jwt = jwt
    }
  },
  actions: {

  }
})
