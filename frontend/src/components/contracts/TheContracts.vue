<template>
  <div class="contracts-table">
    <div class="contracts-table__headers">
      <div class="headers__item">Номер контракта</div>
      <div class="headers__item">Извещение</div>
      <div class="headers__item">Дата подписания</div>
      <div class="headers__item">Цена</div>
      <div class="headers__item">Клиент</div>
      <div class="headers__item">Поставщик</div>
      <div class="headers__item">Регион</div>
      <div class="headers__item">Претензии</div>
    </div>
    <div class="contracts-table__body">
      <div v-for="contract in contracts" :key="contract.id" class="body-line">
        <router-link :to="'/contracts/' + contract.id">
          <div class="body-line__item">{{ contract.number }}</div>
        </router-link>
        <div class="body-line__item">{{ contract.notice }}</div>
        <div class="body-line__item">{{ contract.start_date }}</div>
        <div class="body-line__item">{{ contract.price }}</div>
        <div class="body-line__item">{{ contract.client.name }}</div>
        <div class="body-line__item">{{ contract.company.name }}</div>
        <div class="body-line__item">{{ contract.region.name }}</div>
        <div v-if="contract.claims.length > 0" class="body-line__item">Да</div>
        <div v-else class="body-line__item"></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      contracts: [],
    }
  },

  created() {
    fetch('http://127.0.0.1:8000/api/v1/contract/list')
      .then(response => response.json())
      .then(data => this.contracts = data);
  },
}
</script>

<style scoped>
.contracts-table {
  margin: 1%;
}

.contracts-table__headers,
.body-line {
  display: grid;
  grid-template-areas: "number notice start-date price client company region claim";
  grid-template-columns: 10% 15% 10% 10% 20% 15% 10% 10%;
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

.body-line>a {
  text-decoration: none;
  color: inherit;
}

.body-line>a:hover {
  font-weight: bold;
}
</style>