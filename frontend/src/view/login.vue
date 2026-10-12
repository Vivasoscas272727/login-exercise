<template>
  <div class="login-container">
    <div class="left-side"></div>
    <div class="right-side">
      <div class="form-wrapper">
        
        <h2>Gotham City</h2>
        <p>Bienvenidos a Gotham</p>

        <!-- 1. Evento submit para ejecutar la función de login -->
        <form @submit.prevent="iniciarSesion">
          <!-- 2. v-model para atrapar los datos -->
          <input type="email" v-model="email" placeholder="batman@gotham.com" required />
          <input type="password" v-model="password" placeholder="password" required />
          
          <div class="form-actions">
            <label><input type="checkbox" /> Guardar datos</label>
            <a href="#">Recordar contraseña</a>
          </div>

          <button type="submit">Iniciar sesión</button>
        </form>

        <p class="signup-text">
          ¿No tienes una cuenta? <RouterLink to="/register">Crear cuenta</RouterLink>
        </p>
        <p class="signup-text" style="margin-top: 10px;">
          ¿Tienes un código pendiente? <RouterLink to="/confirm">Confirmar cuenta</RouterLink>
        </p>

      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { RouterLink, useRouter } from 'vue-router'

const router = useRouter()
const email = ref('')
const password = ref('')

const iniciarSesion = async () => {
  try {
    // IMPORTANTE: Asumo que tu ruta en FastAPI se llama "/login"
    const respuesta = await fetch('[https://zpvrcb-ip-190-6-19-151.tunnelmole.net/login](https://zpvrcb-ip-190-6-19-151.tunnelmole.net/login)', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        email: email.value,
        password: password.value
      })
    })

    if (respuesta.ok) {
      // Si FastAPI dice que las credenciales son correctas, lo mandamos al Home
      router.push('/home')
    } else {
      const errorData = await respuesta.json()
      alert("Error: " + (errorData.detail || "Credenciales incorrectas"))
    }
  } catch (error) {
    alert("Fallo la conexión. Motivo: " + error.message)
  }
}
</script>

<style scoped>
@import '../assets/login.css';
</style>