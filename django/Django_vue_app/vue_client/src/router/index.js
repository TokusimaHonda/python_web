import Vue from 'vue'
import VueRouter from 'vue-router'
//import Home from '../views/Home.vue'
import Auth from '@/components/pages/Auth.vue'
import HedgeHogs from '@/components/pages/HedgeHogs'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'HedgeHogs',
    component: HedgeHogs
  },
  {
    path: '/auth',
    name: 'Auth',
    component: Auth
  }
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
