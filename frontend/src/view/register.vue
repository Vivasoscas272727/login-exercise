<template>
  <div class="login-container">
    
    <div class="left-side"></div>

    <div class="right-side">
      <div class="form-wrapper">
        
        <h2>Registro en Gotham</h2>
        <p>Crea tu cuenta para acceder al sistema</p>

        <!-- El evento @submit.prevent evita que la página se recargue al darle al botón -->
        <form @submit.prevent="procesarRegistro">
          <!-- Agregamos v-model a cada input para capturar el texto -->
          <input type="text" v-model="nombre" placeholder="Nombre" required />
          <input type="text" v-model="apellido" placeholder="Apellido" required />
          <input type="tel" v-model="cedula" placeholder="Cédula" required />
          <input type="tel" v-model="telefono" placeholder="Número de teléfono" required />
          <input type="email" v-model="email" placeholder="Correo electrónico" required />
          <input type="password" v-model="password" placeholder="Contraseña" required />

          <button type="submit">Registrarse</button>
        </form>

        <p class="signup-text">
          ¿Ya tienes una cuenta? <RouterLink to="/">Iniciar sesión</RouterLink>
        </p>

      </div>
    </div>
  </div>
</template>

<script setup>
// Importamos 'ref' que nos permite crear variables reactivas
import { ref } from 'vue'
import { RouterLink, useRouter } from 'vue-router'

const router = useRouter()

// 1. Declaramos las variables vacías donde caerá el texto del formulario
const nombre = ref('')
const apellido = ref('')
const cedula = ref('')
const telefono = ref('')
const email = ref('')
const password = ref('')

// 2. La función que se dispara al darle al botón "Registrarse"
const procesarRegistro = async () => {
  try {
    // Empaquetamos los datos en formato JSON
    const datosUsuario = {
      nombre: nombre.value,
      apellido: apellido.value,
      cedula_rif: cedula.value,
      telefono: telefono.value,
      email: email.value,
      password: password.value
    }

    console.log("Enviando datos a FastAPI...", datosUsuario)

    // 3. Enviamos la petición POST a tu backend
    // NOTA: Asegúrate de que tu backend esté corriendo y que esta URL sea la correcta
    const respuesta = await fetch ('https://6vugo9-ip-190-153-16-216.tunnelmole.net/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(datosUsuario)
    })

    // 4. Verificamos si FastAPI dijo que todo salió bien (Status 200)
    if (respuesta.ok) {
      alert("¡Registro exitoso! Te enviaremos un código de confirmación.")
      router.push({ path: '/confirm', query: { email: email.value } })
    } else {
      // Si el servidor arroja un error (ej: correo ya registrado)
      const errorData = await respuesta.json()
 
      alert("Error en el registro: " + JSON.stringify(errorData, null, 2))
    }
  } catch (error) {
    console.error("Error de conexión:", error)
    alert("Fallo la conexión. Motivo: " + error.message)
  }
}
</script>

<style scoped>
@import '../assets/login.css';
</style>