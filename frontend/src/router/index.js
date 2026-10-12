import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../view/login.vue'
import registerView from '../view/register.vue'
import confirmView from '../view/confirm.vue'
import homeView from '../view/home.vue' // 1. Asegúrate de importar el Home aquí arriba

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'login', component: LoginView },
    { path: '/register', name: 'register', component: registerView },
    { path: '/confirm', name: 'confirm', component: confirmView },
    { path: '/home', name: 'home', component: homeView } // 2. Agrega la ruta exacta aquí
  ]
})

export default router