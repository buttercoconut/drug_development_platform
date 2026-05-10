import { createStore } from 'vuex'

const store = createStore({
  state() {
    return {
      user: null,
      settings: {
        theme: 'light',
        language: 'en',
      },
    }
  },
  mutations: {
    setUser(state, user) {
      state.user = user
    },
    setTheme(state, theme) {
      state.settings.theme = theme
    },
    setLanguage(state, language) {
      state.settings.language = language
    },
  },
  actions: {
    login({ commit }, user) {
      // placeholder for real auth
      commit('setUser', user)
    },
    logout({ commit }) {
      commit('setUser', null)
    },
  },
  getters: {
    isAuthenticated(state) {
      return !!state.user
    },
    currentTheme(state) {
      return state.settings.theme
    },
  },
})

export default store
