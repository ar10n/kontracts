<template>
  <div class="modal-overlay">
    <div class="modal">
      <h6>Добавление заказчика</h6>
      <input type="search" @input="clientFilter" ref="inputClient" />
      <ul>
        <li v-for="client in filteredClients" :key="client.id" @click="addClient(client)">
          <span>{{ client.name }}</span>
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
      filteredClients: []
    };
  },
  created() {
    fetch(`${ serverUrl }/api/v1/client/list`, {
      method: 'GET',
      headers: {
        'Authorization': `JWT ${ this.$store.getters['users/getToken'] }`
      }
    })
      .then(response => response.json())
      .then(data => this.$store.dispatch('clients/addClients', { clients: data }));
  },
  components: { BaseButton },
  methods: {
    // Фильтрация по названию
    clientFilter() {
      this.filteredClients = [];
      const clients = this.$store.getters['clients/clients'];
      const inputClient = this.$refs.inputClient.value.toLowerCase();
      if (inputClient.length > 0) {
        clients.filter(
          client => {
            if (client.name.toLowerCase().includes(inputClient)) {
              this.filteredClients.push(client);
            }
          }
        );
      } else {
        this.filteredClients = [];
      }
    },
    // Добавление в форму + закрытие модала
    addClient(client) {
      this.$store.commit('clients/addClient', { client: client });
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