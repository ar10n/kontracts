<template>
  <div>
    <contract-modal v-if="newContractClicked">
      <template #actions>
        <base-button @click="closeContractModal" mode="base">Закрыть</base-button>
      </template>
    </contract-modal>

    <client-modal v-if="newClientClicked">
      <template #actions>
        <base-button @click="closeClientModal" mode="base">Закрыть</base-button>
      </template>
    </client-modal>

    <header>
      <div class="logo">KONTRACTS</div>
      <div class="buttons">
        <header-button @click="toggleClientModal">Новый клиент</header-button>
        <header-button @click="toggleContractModal">Новый контракт</header-button>
        <header-button>Новая претензия</header-button>
      </div>
    </header>
  </div>
</template>

<script>
import BaseButton from '../UI/BaseButton.vue';
import ClientModal from '../UI/ClientModal.vue';
import ContractModal from '../UI/ContractModal.vue';
import HeaderButton from '../UI/HeaderButton.vue';

export default {
  data() {
    return {
      newContractClicked: false,
      newClientClicked: false,
    }
  },
  components: { BaseButton, HeaderButton, ContractModal, ClientModal },
  methods: {
    toggleContractModal() {
      this.newContractClicked = !this.newContractClicked;
    },
    closeContractModal() {
      this.newContractClicked = false;
    },
    toggleClientModal() {
      this.newClientClicked = !this.newClientClicked;
    },
    closeClientModal() {
      this.newClientClicked = false;
    },
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

.logo {
  color: #f1faee;
  font-size: 1.5rem;
  padding-left: 10px;
  cursor: default;
}
</style>
