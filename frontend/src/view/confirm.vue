<!--npx tunnelmole 8000-->
<!--npx tunnelmole 5173-->
<template>
  <div class="login-container">
    <div class="left-side"></div>

    <div class="right-side">
      <div class="form-wrapper">
        
        <h2>Verificar Cuenta</h2>
        <p>Ingresa el código de 6 dígitos que enviamos a tu correo.</p>

        <form @submit.prevent="enviarCodigo">
          <!-- Ya quitamos el campo del correo, solo pedimos el código -->
          <input type="text" v-model="codigo" placeholder="Código de verificación" required />
          
          <button type="submit">Verificar y Entrar</button>
        </form>

        <p class="signup-text">
          ¿No recibiste el código? <a href="#">Reenviar código</a>
        </p>
        
        <p class="signup-text" style="margin-top: 10px;">
          <RouterLink to="/register">Volver al registro</RouterLink>
        </p>

      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
// Agregamos 'useRoute' para poder leer el correo que viene del registro
import { RouterLink, useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()

// Variable para el código que escribe el usuario
const codigo = ref('')

// Atrapamos el correo que pasamos de forma invisible en el Paso 1
const correoUsuario = route.query.email

const enviarCodigo = async () => {
  try {
    console.log("Enviando código para el correo:", correoUsuario)

    const respuesta = await fetch('https://6vugo9-ip-190-153-16-216.tunnelmole.net/verify', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      // Empaquetamos el correo invisible y el código escrito
      body: JSON.stringify({
        email: correoUsuario,
        codigo: codigo.value
      })
    })

    if (respuesta.ok) {
      alert("¡Cuenta verificada con éxito!")
      router.push({ path: '/confirm', query: { email: correo.value } })
    } else {
      const errorData = await respuesta.json()
      alert("Error: " + JSON.stringify(errorData, null, 2))
    }

  } catch (error) {
    console.error("Error de conexión:", error)
    alert("No se pudo conectar con el servidor.")
  }
}
</script>

<style scoped>
@import '../assets/login.css';
</style>