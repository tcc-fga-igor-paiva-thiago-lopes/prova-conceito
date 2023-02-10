import { createRouter, createWebHistory } from '@ionic/vue-router';
import { RouteRecordRaw } from 'vue-router';
import HomePage from '../views/HomePage.vue'
import SignUp from '../views/SignUp.vue';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    redirect: '/signup'
  },
  {
    path: '/home',
    name: 'Home',
    component: HomePage
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUp
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
