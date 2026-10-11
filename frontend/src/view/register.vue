<template>
  <div class="login-container">
    
    <!-- Mitad izquierda (Batman se mantiene aquí) -->
    <div class="left-side"></div>

    <!-- Mitad derecha (Formulario más grande) -->
    <div class="right-side">
      <div class="form-wrapper">
        
        <h2>Registro en Gotham</h2>
        <p>Crea tu cuenta para acceder al sistema</p>

        <form @submit.prevent="procesarRegistro">
          <input type="text" placeholder="Nombre" required />
          <input type="text" placeholder="Apellido" required />
          <input type="text" placeholder="Cédula" required />
          <input type="tel" placeholder="Número de teléfono" required />
          <input type="email" placeholder="Correo electrónico" required />
          <input type="password" placeholder="Contraseña" required />

          <!-- Este es el botón que luego enviará los datos y el correo de confirmación -->
          <button type="submit">Registrarse</button>
        </form>

        <p class="signup-text">
          ¿Ya tienes una cuenta? 
          <!-- RouterLink nos devuelve al Login sin recargar la página -->
          <RouterLink to="/">Iniciar sesión</RouterLink>
        </p>

      </div>
    </div>
  </div>
</template>

<script setup>
import { RouterLink, useRouter } from 'vue-router'
const router = useRouter()
const procesarRegistro = () => {
  
  router.push('/confirm')
}
</script>

<style scoped>
/* Reutilizamos exactamente el mismo diseño */
@import '../assets/login.css';
</style>