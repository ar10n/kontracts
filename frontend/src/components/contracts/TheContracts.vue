<template>
  <details-modal v-if="contractClicked" :contractInfo="contractInfo">
    <template #actions>
      <base-button @click="closeModal">Закрыть</base-button>
    </template>
  </details-modal>

  <div class="contracts-table">
    <div class="contracts-table__headers">
      <div class="headers__item">Номер контракта</div>
      <div class="headers__item">Извещение</div>
      <div class="headers__item">Дата подписания</div>
      <div class="headers__item">Цена</div>
      <div class="headers__item">Клиент</div>
      <div class="headers__item">Поставщик</div>
      <div class="headers__item">Регион</div>
    </div>
    <div class="contracts-table__body">
      <div v-for="contract in contracts" :key="contract.id" class="body-line" @click="toggleModal(contract)">
        <div class="body-line__item">{{ contract.number }}</div>
        <div class="body-line__item">{{ contract.notice }}</div>
        <div class="body-line__item">{{ contract.start_date }}</div>
        <div class="body-line__item">{{ contract.price }}</div>
        <div class="body-line__item">{{ contract.client.name }}</div>
        <div class="body-line__item">{{ contract.company.name }}</div>
        <div class="body-line__item">{{ contract.region.name }}</div>
      </div>
    </div>
  </div>
</template>

<script>
import BaseButton from '../UI/BaseButton.vue';
import DetailsModal from '../UI/DetailsModal.vue';

export default {
  components: { BaseButton, DetailsModal },

  data() {
    return {
      contractInfo: null,
      contracts: null,
      contractClicked: false,
    }
  },

  methods: {
    toggleModal(contract) {
      this.contractInfo = contract;
      this.contractClicked = !this.contractClicked;
    },
    closeModal() {
      this.contractClicked = false;
    }
  },

  created() {
    fetch('http://127.0.0.1:8000/api/v1/contract/list')
      .then(response => response.json())
      .then(data => this.contracts = data);
  }
}
</script>

<style scoped>
.contracts-table {
  margin: 1%;
}

.contracts-table__headers,
.body-line {
  display: grid;
  grid-template-areas: "number notice start-date price client company region";
  grid-template-columns: 15% 15% 10% 15% 25% 10% 10%;
  padding-top: 1%;
  padding-bottom: 1%;
  cursor: default;
}

.contracts-table__headers {
  border-bottom: 1px solid #1d3557;
}

.headers__item {
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  font-weight: 500;
  border-right: 1px solid #1d3557;
}

.headers__item:last-child,
.body-line__item:last-child {
  border-right: none;
}

.body-line {
  border-radius: 10px;
}

.body-line:hover {
  background-color: #f1faee;
  border-radius: 10px;
}

.body-line:hover>.body-line__item {
  border-right: 1px solid #1d3557;
}

.body-line:hover>.body-line__item:last-child {
  border-right: none;
}

.body-line__item {
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  border-right: 1px solid #1d3557;
  font-size: 0.9rem;
}
</style>