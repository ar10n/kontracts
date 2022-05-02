<template>
  <div class="contract-details">
    <div class="details">
      <h2>Договор №{{ contract.number }} от {{ contract.start_date }}</h2>
      <h3>{{ contract.client.name }}</h3>
      <div class="client">
        <div>ИНН {{ contract.client.inn }}</div>
        <div v-if="contract.client.phone.lenght > 0">Телефон: {{ contract.client.phone }}</div>
        <div v-else>Телефон отсутствует</div>
        <div v-if="contract.client.email.lenght > 0">Email: {{ contract.client.email }}</div>
        <div v-else>Email отсутствует</div>
        <div v-if="contract.client.comment.lenght > 0">Комментарий: {{ contract.client.comment }}</div>
      </div>
      <div class="line"></div>
      <div>Поставщик: {{ contract.company.name }}</div>
      <div>Регион: {{ contract.region.name }}</div>
      <div>Срок действия: {{ contract.end_date }}</div>
      <div>Товары:</div>
      <div v-for="product in contract.products" :key="product.id">
        {{ product.name }} ({{ product.manufacturer.name }})
      </div>
      <div>Цена: {{ contract.price }}</div>
      <div v-if="contract.is_done === false">Договор на стадии исполнения</div>
      <div v-else>Договор исполнен</div>
    </div>
    <div class="claims">
      <h2>Претензии</h2>
      <div>{{ contract }}</div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      contract: undefined
    }
  },

  created() {
    const id = this.$route.params.id;
    const url = `http://127.0.0.1:8000/api/v1/contract/${ id }`

    fetch(url)
      .then(response => response.json())
      .then(data => this.contract = data);
  }
}
</script>

<style scoped>
.contract-details {
  display: grid;
  grid-template-areas: "details claims";
  grid-template-columns: 60% 40%;
}

.details {
  border-right: 1px solid #1d3557;
  padding: 1rem;
  height: calc(95vh - 2rem);
}

.claims {
  padding: 1rem;
}

.client {
  display: flex;
  justify-content: space-between;
}

h2 {
  text-align: center;
}

.line {
  display: block;
  border-bottom: 1px solid #1d3557;
  margin-top: 0.5rem;
  margin-bottom: 0.5rem;
}
</style>