<template>
  <header>
    <div class="logo">KONTRACTS</div>
    <div class="buttons">
      <header-button @click="toggleModal">Добавить контракт</header-button>
      <header-button>Добавить претензию</header-button>
    </div>
  </header>
</template>

<script>
import HeaderButton from '../UI/HeaderButton.vue';

export default {
  data() {
    return {
      newContractClicked: false,
    }
  },
  components: { HeaderButton },
  methods: {
    toggleModal() {
      this.newContractClicked = !this.newContractClicked;
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
}

.logo {
  color: #f1faee;
  font-size: 1.5rem;
  padding-left: 10px;
  cursor: default;
}
</style>
