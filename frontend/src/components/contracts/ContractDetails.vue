<template>
  <div class="contract-details">
    <div class="details">

      <div class="custom-h">Договор №{{ contract.number }} от {{ contract.start_date }}</div>

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
      <div>Кол-во дней на поставку: {{ contract.days_to_deliver }}</div>
      <div>Срок оплаты: {{ contract.days_to_pay }}</div>

      <div class="line"></div>

      <div>Товары:</div>
      <div v-for="product in contract.products" :key="product.id">
        {{ product.name }} ({{ product.manufacturer.name }})
      </div>

      <div class="line"></div>

      <div class="custom-h">Претензии</div>
      <div v-if="contract.claims.length > 0">
        <div v-for="claim in contract.claims" :key="claim.id" class="claim">
          <div class="claim-name">{{ claim.name }} от {{ claim.start_date }}</div>
          <div class="claim-deadline">Срок: {{ claim.deadline }}</div>
          <div class="claim-comment">Комментарий: {{ claim.comment }}</div>
        </div>
      </div>
      <div v-else>Претензии отсутствуют</div>

    </div>

    <div class="right-side">

      <div class="custom-h">Отгрузки</div>
      <div v-if="contract.shipments.length > 0">
        <div class="shipments-header">
          <div>№</div>
          <div>Цена</div>
          <div>Отгрузка</div>
          <div>Доставка</div>
          <div>Оплата</div>
        </div>
        <div v-for="shipment in contract.shipments" :key="shipment.id" class="shipments">
          <div class="shipments-line">
            <div class="shipments-line__item">{{ shipment.number }}</div>
            <div class="shipments-line__item">{{ shipment.price }}</div>
            <div class="shipments-line__item">{{ shipment.start_date }}</div>
            <div class="shipments-line__item">
              <span v-if="shipment.is_delivered === true">{{ shipment.delivery_date }}</span>
              <span v-else class="false">{{ shipment.delivery_date }}</span>
            </div>
            <div class="shipments-line__item">
              <span v-if="shipment.pay_date === true">{{ shipment.pay_date }}</span>
              <span v-else class="false">{{ shipment.pay_date }}</span>
            </div>
          </div>
        </div>
      </div>
      <div v-else>Отгрузки отсутствуют</div>

    </div>

  </div>
</template>

<script>
import { serverUrl } from '../../config.js';

export default {
  created() {
    const id = this.$route.params.id;
    const url = `${ serverUrl }/api/v1/contract/${ id }`;

    fetch(url, {
      method: 'GET',
      headers: {
        'Authorization': `JWT ${ this.$store.getters['users/getToken'] }`
      }
    })
      .then(response => response.json())
      .then(data => this.$store.dispatch('cons/addContractDetails', { contract: data }));
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

.custom-h {
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

.claim,
.shipments {
  padding-bottom: 1rem;
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

.right-side {
  padding: 1rem;
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

.shipments-header,
.shipments-line {
  display: grid;
  grid-template-areas: "number price start-date days-to-deliver days-to-pay";
  grid-template-columns: 20% 20% 20% 20% 20%;
  padding-top: 1%;
  padding-bottom: 1%;
  text-align: center;
}

.shipments-header {
  font-weight: bold;
}

.shipments-line {
  background-color: #A8DADC;
  border-radius: 10px;
}

.shipments-line__item {
  padding: 1rem;
  font-size: 0.9rem;
}

.false {
  color: #E63946;
  font-weight: bold;
  font-size: 0.9rem;
}

.line {
  display: block;
  border-bottom: 1px solid #1d3557;
  margin-top: 0.5rem;
  margin-bottom: 0.5rem;
}
</style>