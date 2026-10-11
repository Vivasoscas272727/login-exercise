import { createRouter, createWebHistory } from 'vue-router'
// Ajustamos las rutas para que coincidan con tu carpeta "view" y tus archivos en minúsculas
import LoginView from '../view/login.vue'
import registerView from '../view/register.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: LoginView
    },
    {
      path: '/register',
      name: 'register',
      component: registerView
    }
  ]
})

export default router