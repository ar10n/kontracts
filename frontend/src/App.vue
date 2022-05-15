<template>
  <the-header class="header"></the-header>
  <router-view></router-view>
</template>

<script>
import TheHeader from './components/layouts/TheHeader.vue';

export default {
  components: {TheHeader},
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Exo+2:ital,wght@0,300;0,400;0,500;0,700;1,300;1,400;1,500;1,700&display=swap");

html {
  font-family: "Exo 2", sans-serif;
}

body {
  margin: 0;
}

.header {
  position: sticky;
  top: 0;
}
</style>