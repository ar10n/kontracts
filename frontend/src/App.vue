<template>
  <div v-if="isLoggedIn == true">
    <the-header class="header"></the-header>
    <router-view></router-view>
  </div>
  <div v-else>
    <sign-in></sign-in>
  </div>
</template>

<script>
import SignIn from './components/auth/SignIn.vue';
import TheHeader from './components/layouts/TheHeader.vue';

export default {
  components: { TheHeader, SignIn },

  computed: {
    isLoggedIn() {
      return this.$store.getters['users/getToken'] ? true : false;
    }
  }
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