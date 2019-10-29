import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user_id: '',
    user_jwt: '',
    user_name: '',
    // baseUrl: "http://54.180.148.99:8000/"
    baseUrl: 'http://localhost:8000/'
  },
  plugins: [createPersistedState()],
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
