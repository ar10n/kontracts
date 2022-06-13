<template>
  <div>
    <header>
      <router-link to="/">
        KONTRACTS
      </router-link>

      <div class="menu" @click="isOpen = !isOpen" v-if="isLoggedIn == true">
        МЕНЮ
        <transition name="fade" appear>
          <div class="sub-menu" v-if="isOpen">
            <router-link to="/shipments/create">
              Добавить отгрузку
            </router-link>
            <router-link to="/claims/create">
              Добавить претензию
            </router-link>
            <router-link to="/clients/create">
              Добавить клиента
            </router-link>
            <router-link to="/contracts/create">
              Добавить контракт
            </router-link>
          </div>
        </transition>
      </div>
    </header>
  </div>
</template>

<script>
import { RouterLink } from 'vue-router';

export default {
  data() {
    return {
      isOpen: false,
    }
  },
  components: { RouterLink },
  computed: {
    isLoggedIn() {
      return this.$store.getters['users/getToken'] ? true : false;
    }
  }
}
</script>

<style scoped>
header {
  background-color: #1d3557;
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 5vh;
}

header>a {
  text-decoration: none;
  padding: 0.3rem;
  margin: 0.3rem;
  color: #f1faee;
}

.sub-menu>a,
.menu {
  text-decoration: none;
  font-size: 0.8rem;
  padding: 0.3rem;
  margin: 0.3rem;
  border: 1px solid #f1faee;
  border-radius: 5px;
  background-color: #1d3557;
  color: #f1faee;
}

.menu {
  position: relative;
  cursor: pointer;
  display: flex;
  transition: 0.4s;
}

.sub-menu {
  position: absolute;
  top: calc(100% + 18px);
  right: calc(100% - 45px);
  width: max-content;
  display: flex;
  flex-direction: column;
  background-color: #1d3557;
  border: 1px solid #f1faee;
  border-radius: 5px;
  padding: 10%;
  text-align: center;
}

.sub-menu>a:hover {
  background-color: #f1faee;
  color: #1d3557;
  transition: all 300ms ease-out;
}

.sub-menu>.router-link-active {
  background-color: #f1faee;
  color: #1d3557;
  cursor: not-allowed;
}

.fade-enter-active,
.fade-leave-active {
  transition: all .2s ease-out;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
