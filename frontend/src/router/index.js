import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import DrugDevelopment from '../views/DrugDevelopment.vue'
import Analytics from '../views/Analytics.vue'
import Settings from '../views/Settings.vue'

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/drug-development', name: 'DrugDevelopment', component: DrugDevelopment },
  { path: '/analytics', name: 'Analytics', component: Analytics },
  { path: '/settings', name: 'Settings', component: Settings },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
