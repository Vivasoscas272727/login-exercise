<template>
  <div class="login-container">
    
    <!-- Mitad izquierda (Batman en Gotham) -->
    <div class="left-side"></div>

    <!-- Mitad derecha (Formulario) -->
    <div class="right-side">
        <div class="form-wrapper">
        
        <h2>Gotham City</h2>
        <p>Bienvenidos a Gotham</p>

        <form>
          <input type="email" placeholder="batman@gotham.com" required />
          <input type="password" placeholder="password" required />
          
          <div class="form-actions">
            <label><input type="checkbox" /> Remember me</label>
            <a href="#">Recordar contraseña</a>
          </div>

          <button type="submit">iniciar sesion</button>
        </form>

        <p class="signup-text">
          ¿no tienes una cuenta? <RouterLink to="/register">Crear cuenta</RouterLink>
        </p>

      </div>
    </div>
  </div>
</template>

<style scoped>
@import '../assets/login.css';
</style>

<script setup>
import { RouterLink } from 'vue-router'
</script>