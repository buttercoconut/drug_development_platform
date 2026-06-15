import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import DrugCandidates from '../views/DrugCandidates.vue'
import ClinicalData from '../views/ClinicalData.vue'

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/drug-candidates', name: 'DrugCandidates', component: DrugCandidates },
  { path: '/clinical-data', name: 'ClinicalData', component: ClinicalData },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
