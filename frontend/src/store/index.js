import { createStore } from 'vuex'

export default createStore({
  state: {
    drugCandidates: [],
    clinicalData: [],
  },
  mutations: {
    setDrugCandidates(state, payload) {
      state.drugCandidates = payload
    },
    setClinicalData(state, payload) {
      state.clinicalData = payload
    },
  },
  actions: {
    fetchDrugCandidates({ commit }) {
      // placeholder for API call
      commit('setDrugCandidates', [])
    },
    fetchClinicalData({ commit }) {
      commit('setClinicalData', [])
    },
  },
})
