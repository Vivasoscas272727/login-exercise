<template>
  <div class="login-container">
    
    <!-- Mitad izquierda (Batman) -->
    <div class="left-side"></div>

    <!-- Mitad derecha (Formulario del Código) -->
    <div class="right-side">
      <div class="form-wrapper">
        
        <h2>Verificar Cuenta</h2>
        <p>Ingresa el código de 6 dígitos que enviamos a tu correo.</p>

        <form>
          <input type="text" placeholder="Código de verificación" required />
          <button type="submit">Verificar y Entrar</button>
        </form>

        <p class="signup-text">
          ¿No recibiste el código? <a href="#">Reenviar código</a>
        </p>
        
        <!-- Botón para volver por si se equivocó de correo -->
        <p class="signup-text" style="margin-top: 10px;">
          <RouterLink to="/register">Volver al registro</RouterLink>
        </p>

      </div>
    </div>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<style scoped>
@import '../assets/login.css';
</style>