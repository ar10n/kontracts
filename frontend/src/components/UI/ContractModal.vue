<template>
  <div class="background"></div>
  <dialog open>
    <header>
      <div>Новый контракт</div>
    </header>
    <section>
      <form @submit.prevent="submitData">
        <div class="form-line">
          <div class="line-element">
            <label class="bold-label" for="number">Номер контракта</label>
            <input id="number" name="number" type="text" ref="numberInput">
          </div>
          <div class="line-element">
            <label class="bold-label" for="notice_number">Номер извещения</label>
            <input id="notice_number" name="notice_number" type="text" ref="noticeNumberInput">
          </div>
        </div>
        <div class="form-line">
          <div class="line-element">
            <label class="bold-label" for="start_date">Дата подписания</label>
            <input id="start_date" name="start_date" type="date" ref="startDateInput">
          </div>
          <div class="line-element">
            <label class="bold-label" for="end_date">Срок действия</label>
            <input id="end_date" name="end_date" type="date" ref="endDateInput">
          </div>
        </div>
        <div class="form-line">
          <div class="line-element">
            <label class="bold-label" for="client">Заказчик</label>
            <select id="client" name="client" ref="clientInput">
              <option v-for="client in clients" :key="client.id" :value="client.id">{{ client.name }}</option>
            </select>
          </div>
          <div class="line-element">
            <label class="bold-label" for="company">Поставщик</label>
            <select id="company" name="company" ref="companyInput">
              <option :value="company.id" v-for="company in companies" :key="company.id">{{ company.name }}</option>
            </select>
          </div>
        </div>
        <div class="form-line">
          <div class="line-element">
            <label class="bold-label" for="price">Стоимость</label>
            <input id="price" name="price" type="text" ref="priceInput">
          </div>
          <div class="line-element">
            <label class="bold-label" for="region">Регион</label>
            <select id="region" name="region" ref="regionInput">
              <option :value="region.id" v-for="region in regions" :key="region.id">{{ region.name }}</option>
            </select>
          </div>
        </div>
        <div class="form-line">
          <div class="line-element">
            <label class="bold-label" for="products">Товары</label>
            <select multiple size="5" id="products" name="products" ref="productsInput">
              <option :value="product.id" v-for="product in products" :key="product.id">{{ product.name }}</option>
            </select>
          </div>
          <div class="line-element">
            <div class="bold-label">Признак выполнения</div>
            <div class="radio">
              <div class="radio-line">
                <label for="done">Выполнен</label>
                <input id="done" name="isdone" type="radio">
              </div>
              <div class="radio-line">
                <label for="undone">Не выполнен</label>
                <input id="undone" name="isdone" type="radio">
              </div>
            </div>
          </div>
        </div>
        <menu class="buttons">
          <div>
            <base-button type="submit" mode="submit">Создать</base-button>
          </div>
          <slot name="actions"></slot>
        </menu>
      </form>
    </section>
  </dialog>
</template>

<script>
import BaseButton from './BaseButton.vue';

export default {
  data() {
    return {
      clients: [],
      companies: [],
      regions: [],
      products: []
    }
  },
  components: { BaseButton },
  methods: {
    submitData() {
      const numberInput = this.$refs.numberInput.value;
      const noticeNumberInput = this.$refs.noticeNumberInput.value;
      const startDateInput = this.$refs.startDateInput.value;
      const endDateInput = this.$refs.endDateInput.value;
      const priceInput = this.$refs.priceInput.value;
      const clientInput = this.$refs.clientInput.value;

      console.log(numberInput, noticeNumberInput, startDateInput, endDateInput, priceInput, clientInput);
    }
  },
  created() {
    fetch('http://127.0.0.1:8000/api/v1/client/list')
      .then(response => response.json())
      .then(data => this.clients = data);
    fetch('http://127.0.0.1:8000/api/v1/company/list')
      .then(response => response.json())
      .then(data => this.companies = data);
    fetch('http://127.0.0.1:8000/api/v1/region/list')
      .then(response => response.json())
      .then(data => this.regions = data);
    fetch('http://127.0.0.1:8000/api/v1/product/list')
      .then(response => response.json())
      .then(data => this.products = data);
  },
  props: ['contractInfo'],
}
</script>

<style scoped>
.radio-line {
  display: flex;
  justify-content: space-between;
  margin-top: 1rem;
}

.bold-label {
  font-weight: bold;
}

select,
input {
  font-family: inherit;
}

.form-line {
  display: flex;
  justify-content: space-around;
  margin-bottom: 0.5rem;
}

.line-element {
  display: flex;
  flex-direction: column;
  width: 45%;
}

.background {
  position: fixed;
  top: 0;
  left: 0;
  height: 100vh;
  width: 100%;
  background-color: rgba(0, 0, 0, 0.55);
  z-index: 10;
}

dialog {
  position: fixed;
  top: 10vh;
  left: 20%;
  right: 20%;
  width: 60%;
  z-index: 100;
  border-radius: 5px;
  border: none;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
  padding: 0;
  margin: 0;
  overflow: hidden;
}

header {
  background-color: #1D3557;
  color: #F1FAEE;
  width: 100%;
  padding-top: 1rem;
  padding-bottom: 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

header>div {
  padding-right: 1.5rem;
  padding-left: 1.5rem;
  font-size: 1.5rem;
}

section {
  padding: 1rem;
}

section>div {
  padding: 0.5rem;
}

menu {
  padding: 1.5rem;
  display: flex;
  justify-content: flex-end;
  margin: 0;
}

.buttons {
  display: flex;
  justify-content: space-between;
}
</style>