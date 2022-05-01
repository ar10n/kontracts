<template>
  <div class="container">
    <the-header></the-header>
    <the-body class="the-body"></the-body>
  </div>
</template>

<script>
import TheBody from './components/layouts/TheBody.vue';
import TheHeader from './components/layouts/TheHeader.vue';

export default {
  components: { TheBody, TheHeader }
}
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Exo+2:ital,wght@0,300;0,400;0,500;0,700;1,300;1,400;1,500;1,700&display=swap");

html {
  font-family: "Exo 2", sans-serif;
}

body {
  margin: 0;
}

.container {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.the-body {
  height: 95vh;
}
</style>