<template>
  <div class="modal-overlay">
    <div class="modal">
      <h6>Добавление поставщика</h6>
      <input type="search" @input="companyFilter" ref="inputCompany" />
      <ul>
        <li v-for="company in filteredCompanies" :key="company.id" @click="addCompany(company)">
          <span>{{ company.name }}</span>
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
      filteredCompanies: []
    };
  },
  created() {
    fetch(`${ serverUrl }/api/v1/company/list`, {
      method: 'GET',
      headers: {
        'Authorization': `JWT ${ this.$store.getters['users/getToken'] }`
      }
    })
      .then(response => response.json())
      .then(data => this.$store.dispatch('comps/addCompanies', { companies: data }));
  },
  components: { BaseButton },
  methods: {
    // Фильтрация по названию компании
    companyFilter() {
      this.filteredCompanies = [];
      const companies = this.$store.getters['comps/companies'];
      const inputCompany = this.$refs.inputCompany.value.toLowerCase();
      if (inputCompany.length > 0) {
        companies.filter(
          company => {
            if (company.name.toLowerCase().includes(inputCompany)) {
              this.filteredCompanies.push(company);
            }
          }
        );
      } else {
        this.filteredCompanies = [];
      }
    },
    // Добавление компании в форму с закрытием модала
    addCompany(company) {
      this.$store.commit('comps/addCompany', { company: company });
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