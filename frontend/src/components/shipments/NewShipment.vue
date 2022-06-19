<template>
  <h2>Новая отгрузка</h2>

  <form @submit.prevent="submitData">

    <div class="form-line">
      <div class="form-line__item first-line-item">
        <label for="number">Номер накладной</label>
        <input id="number" name="number" type="text" ref="numberInput">
      </div>
      <div class="form-line__item first-line-item">
        <label for="price">Сумма</label>
        <input id="price" name="price" type="number" ref="priceInput">
      </div>
    </div>

    <div class="form-line">
      <div class="form-line__item second-line-item">
        <label for="start-date">Дата документа</label>
        <input id="start-date" name="start-date" type="date" ref="startDateInput">
      </div>
      <div class="form-line__item second-line-item">
        <label for="delivery-date">Дата доставки</label>
        <input id="delivery-date" name="delivery-date" type="date" ref="deliveryDateInput">
      </div>
      <div class="form-line__item second-line-item">
        <label for="pay-date">Дата оплаты</label>
        <input id="pay-date" name="pay-date" type="date" ref="payDateInput">
      </div>
    </div>

    <div class="form-line">
      <div class="form-line__item second-line-item">
        <div>Контракт</div>
        <div v-if="contract.length < 1" @click="contractModal = true">
          <base-button>Добавить</base-button>
        </div>
        <div v-else class="selected-item">{{ contract.number }}<span @click="removeContract">X</span></div>
      </div>
      <div class="form-line__item second-line-item">
        <div>Доставлено? <span>(не обязательно)</span></div>
        <div class="checkbox">
          <label for="delivered">Да</label>
          <input type="checkbox" name="delivered" ref="isDelivered">
        </div>
      </div>
      <div class="form-line__item second-line-item">
        <div>Оплачено? <span>(не обязательно)</span></div>
        <div class="checkbox">
          <label for="paid">Да</label>
          <input type="checkbox" name="paid" ref="isPaid">
        </div>
      </div>
    </div>

    <div class="form-line">
      <div>
        <base-button type="submit" mode="submit">Создать</base-button>
      </div>
    </div>

  </form>

  <contract-modal v-show="contractModal" @close-modal="contractModal = false"></contract-modal>
</template>

<script>
import { serverUrl } from '../../config.js';
import BaseButton from "../UI/BaseButton.vue";
import ContractModal from "../UI/ContractModal.vue";

export default {
  data() {
    return {
      contractModal: false
    };
  },
  name: "NewShipment",
  components: { BaseButton, ContractModal },
  computed: {
    contract() {
      return this.$store.getters['cons/contractInClaim'];
    }
  },
  methods: {
    submitData() {
      const data = {
        number: this.$refs.numberInput.value,
        price: this.$refs.priceInput.value,
        start_date: this.$refs.startDateInput.value,
        delivery_date: this.$refs.deliveryDateInput.value,
        pay_date: this.$refs.payDateInput.value,
        is_delivered: this.$refs.isDelivered.checked,
        is_paid: this.$refs.isPaid.checked,
        contract: this.$store.getters['cons/contractInClaim'].id
      };

      try {
        fetch(`${ serverUrl }/api/v1/shipment/create`, {
          method: 'POST',
          body: JSON.stringify(data),
          headers: {
            'Content-Type': 'application/json'
          }
        });
        this.$store.commit('cons/removeContract');
      } catch (e) {
        console.log(e);
      }
    },
    removeContract() {
      this.$store.commit('cons/removeContract');
    }
  }
};
</script>

<style scoped>
h2 {
  color: #1d3557;
  text-align: center;
}

input {
  font-family: inherit;
  margin: 5px;
  padding: 5px;
  border-radius: 5px;
  border: 1px solid #1d3557;
}

form {
  display: flex;
  flex-direction: column;
}

.form-line {
  display: flex;
  justify-content: center;
}

.form-line__item {
  display: flex;
  flex-direction: column;
  padding: 1rem;
}

.first-line-item {
  width: 23.5rem;
}

.second-line-item {
  width: 15rem;
}

label>span,
div>span {
  font-size: 0.7rem;
  font-style: italic;
}

button,
.checkbox {
  margin: 5px;
  padding: 5px;
}

.selected-item>span {
  margin-left: 5px;
  font-weight: bold;
  color: #E63946;
  cursor: pointer;
}
</style>