<script>
import TheBody from './components/layouts/TheBody.vue';
import TheHeader from './components/layouts/TheHeader.vue';

export default {
  components: { TheBody, TheHeader }
}
</script>

<template>
  <div class="container">
    <TheHeader class="the-header"></TheHeader>
    <TheBody class="the-body"></TheBody>
  </div>
</template>

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

.the-header {
  height: 5vh;
}

.the-body {
  height: 95vh;
}
</style>