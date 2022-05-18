<template>
  <div class="contract-details">
    <div class="details">

      <div class="client-header">Договор №{{ contract.number }} от {{ contract.start_date }}</div>

      <div class="client">
        <div class="client-name">Заказчик: {{ contract.client.name }}</div>
        <div class="is-done">
          <div class="not-done" v-if="contract.is_done === false">Договор на стадии исполнения</div>
          <div class="done" v-else>Договор исполнен</div>
        </div>
      </div>

      <div class="client-details">
        <div>ИНН {{ contract.client.inn }}</div>
        <div v-if="contract.client.phone">Телефон: {{ contract.client.phone }}</div>
        <div v-else>Телефон отсутствует</div>
        <div v-if="contract.client.email">Email: {{ contract.client.email }}</div>
        <div v-else>Email отсутствует</div>
        <div v-if="contract.client.comment">Комментарий: {{ contract.client.comment }}</div>
      </div>

      <div class="line"></div>

      <div>Поставщик: {{ contract.company.name }}</div>
      <div>Регион: {{ contract.region.name }}</div>
      <div>Срок действия: {{ contract.end_date }}</div>
      <div>Цена: {{ contract.price }}</div>
      <div class="line"></div>
      <div>Товары:</div>
      <div v-for="product in contract.products" :key="product.id">
        {{ product.name }} ({{ product.manufacturer.name }})
      </div>

    </div>

    <div class="claims">
      <div class="claim-header">Претензии</div>
      <div v-if="contract.claims.length > 1"><div v-for="claim in contract.claims" :key="claim.id">
        <div class="claim-name">{{ claim.name }} от {{ claim.start_date }}</div>
        <div class="claim-deadline">Срок: {{ claim.deadline }}</div>
        <div class="claim-comment">Комментарий: {{ claim.comment }}</div>
      </div></div>
      <div v-else>
        Претензии отсутствуют
      </div>
    </div>

  </div>
</template>

<script>

export default {
  created() {
    const id = this.$route.params.id;
    const url = `http://127.0.0.1:8000/api/v1/contract/${id}`;

    fetch(url)
      .then(response => response.json())
      .then(data => this.$store.dispatch('cons/addContractDetails', {contract: data}));
  },
  computed: {
    contract() {
      return this.$store.getters['cons/contract'];
    }
  }
};
</script>

<style scoped>
.contract-details {
  display: grid;
  grid-template-areas: "details claims";
  grid-template-columns: 55% 45%;
}

.details {
  border-right: 1px solid #1d3557;
  padding: 1rem;
  height: calc(95vh - 2rem);
}

.client-header {
  display: flex;
  justify-content: center;
  padding-bottom: 2rem;
  font-size: 1.5rem;
  font-weight: bold;
  color: #1d3557;
}

.client {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-bottom: 10px;
}

.client-name {
  font-size: 1.1rem;
  font-weight: bold;
}

.done {
  font-size: 1.1rem;
  color: #1d3557;
}

.not-done {
  border: 1px solid #E63946;
  background-color: #E63946;
  border-radius: 5px;
  color: white;
  padding-left: 0.5rem;
  padding-right: 0.5rem;
  padding-bottom: 0.2rem;
}

.client-details {
  display: flex;
  justify-content: space-between;
}

.claims {
  padding: 1rem;
}

.claim-header {
  display: flex;
  justify-content: center;
  padding-bottom: 2rem;
  font-size: 1.5rem;
  font-weight: bold;
  color: #1d3557;
}

.claim-name {
  background-color: #457B9D;
  padding: 0.5rem;
  border-radius: 10px 10px 0 0;
  color: #F1FAEE;
}

.claim-deadline {
  background-color: #A8DADC;
  padding: 0.5rem;
  border-top: none;
  border-bottom: none;
  color: #1D3557;
}

.claim-comment {
  background-color: #A8DADC;
  padding: 0.5rem;
  border-radius: 0 0 10px 10px;
  border-top: none;
  color: #1D3557;
}

.line {
  display: block;
  border-bottom: 1px solid #1d3557;
  margin-top: 0.5rem;
  margin-bottom: 0.5rem;
}
</style>