<template>
  <div class="home-container">
    <div class="content-wrapper">
      <h1 class="title">BIENVENIDO A LA BATICUEVA</h1>
      <p class="subtitle">Has iniciado sesión correctamente.</p>
      
      <div class="image-box">
        <img src="../assets/imagen2.jpg" alt="Foto de bienvenida" class="foto-perfil" />
      </div>
      
      <RouterLink to="/" class="logout-btn">Cerrar sesión</RouterLink>
    </div>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<style scoped>
/* Fondo completamente negro y centrado absoluto */
.home-container {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background-color: #000000;
  font-family: 'Arial', sans-serif;
  padding: 20px;
  box-sizing: border-box;
}

/* Contenedor principal sin adornos */
.content-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  width: 100%;
  max-width: 800px; /* Permitimos que se expanda más */
}

/* Título imponente en amarillo Batman */
.title {
  font-size: 2.8rem;
  font-weight: 900;
  color: #f1c40f;
  margin: 0 0 5px 0;
  letter-spacing: 1px;
}

/* Subtítulo simple en gris */
.subtitle {
  font-size: 1.2rem;
  color: #888888;
  margin: 0 0 30px 0;
}

/* Contenedor que le da el tamaño "grande" a la imagen */
.image-box {
  width: 100%;
  max-width: 480px; /* Aumentamos el tamaño máximo */
  margin-bottom: 30px;
}

/* La imagen grande que se adapta a la pantalla */
.foto-perfil {
  width: 100%;
  height: auto;
  max-height: 65vh; /* Evita que la imagen vertical empuje todo fuera de la pantalla */
  object-fit: contain;
  border-radius: 8px;
}

/* Botón simple y limpio */
.logout-btn {
  padding: 12px 40px;
  background-color: #e74c3c;
  color: #ffffff;
  text-decoration: none;
  border-radius: 6px;
  font-weight: bold;
  font-size: 1rem;
  transition: background-color 0.2s;
}

.logout-btn:hover {
  background-color: #c0392b;
}

/* Ajustes para pantallas pequeñas (móviles) */
@media (max-width: 600px) {
  .title {
    font-size: 2rem;
  }
  .subtitle {
    font-size: 1rem;
  }
  .image-box {
    max-width: 90%;
  }
}
</style>