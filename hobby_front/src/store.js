import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate"

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user_id: '',
    user_jwt: '',
    user_name: '',
    user_point: '',
    baseUrl: '',
    search_word: ''
  },
  plugins: [createPersistedState()],
  mutations: {
    urlSave(state, url){
      state.baseUrl = url
    },
    idSave (state, id) {
      state.user_id = id
    },
    jwtSave (state, jwt) {
      state.user_jwt = jwt
    },
    nameSave (state, name){
      state.user_name = name
    },
    pointSave (state, point){
      state.user_point = point
    },
    wordSave (state, word) {
      state.search_word = word
    }
  },
  actions: {

  }
})
