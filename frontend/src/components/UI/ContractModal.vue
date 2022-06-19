<template>
  <div class="modal-overlay">
    <div class="modal">
      <h6>Добавление контракта</h6>
      <input type="search" @input="contractFilter" ref="inputContract" />
      <ul>
        <li v-for="contract in filteredContracts" :key="contract.id" @click="addContract(contract)">
          <span>{{ contract.number }}</span>
        </li>
      </ul>
      <base-button @click="$emit('close-modal')">Закрыть</base-button>
    </div>
  </div>
</template>

<script>
import { serverUrl } from '../../config.js';
import BaseButton from "./BaseButton.vue";

export default {
  data() {
    return {
      filteredContracts: []
    };
  },
  created() {
    fetch(`${ serverUrl }/api/v1/contract/list`, {
      method: 'GET',
      headers: {
        'Authorization': `JWT ${ this.$store.getters['users/getToken'] }`
      }
    })
      .then(response => response.json())
      .then(data => this.$store.dispatch('cons/addContracts', { contracts: data }));
  },
  components: { BaseButton },
  methods: {
    // Фильтрация по названию
    contractFilter() {
      this.filteredContracts = [];
      const contracts = this.$store.getters['cons/contracts'];
      const inputContract = this.$refs.inputContract.value.toLowerCase();
      if (inputContract.length > 0) {
        contracts.filter(
          contract => {
            if (contract.number.toLowerCase().includes(inputContract)) {
              this.filteredContracts.push(contract);
            }
          }
        );
      } else {
        this.filteredContracts = [];
      }
    },
    // Добавление в форму + закрытие модала
    addContract(contract) {
      this.$store.commit('cons/addContract', { contract: contract });
      this.$emit('close-modal');
    }
  }
};
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  display: flex;
  justify-content: center;
  background-color: #000000da;
}

.modal {
  text-align: center;
  background-color: white;
  height: 50%;
  width: 50%;
  margin-top: 10%;
  border-radius: 20px;
}

h6 {
  font-weight: 500;
  font-size: 28px;
}

input {
  font-family: inherit;
  margin: 5px;
  padding: 5px;
  border-radius: 5px;
  border: 1px solid #1d3557;
}

ul {
  padding: 0;
}

li {
  list-style-type: none;
  padding: 1%;
}

span:hover {
  color: #E63946;
  cursor: pointer;
  font-weight: bold;
}

button {
  background-color: #E63946;
  width: 150px;
  height: 40px;
  color: white;
  font-size: 14px;
  border-radius: 16px;
  margin-top: 50px;
}
</style>