<template>
  <h2>Новый контракт</h2>

  <form @submit.prevent="submitData">

    <!-- Номер контракта и номер извещения -->
    <div class="form-line">
      <div class="form-line__item">
        <label for="number">Номер контракта</label>
        <input id="number" name="number" type="text" ref="numberInput">
      </div>
      <div class="form-line__item">
        <label for="notice_number">Номер извещения <span>(не обязательно)</span></label>
        <input id="notice_number" name="notice_number" type="text" ref="noticeNumberInput">
      </div>
    </div>

    <!-- Дата подписания и срок действия -->
    <div class="form-line">
      <div class="form-line__item">
        <label for="start_date">Дата подписания</label>
        <input id="start_date" name="start_date" type="date" ref="startDateInput">
      </div>
      <div class="form-line__item">
        <label for="end_date">Срок действия <span>(не обязательно)</span></label>
        <input id="end_date" name="end_date" type="date" ref="endDateInput">
      </div>
    </div>

    <!-- Выбор заказчика и выбор поставщика -->
    <div class="form-line">
      <div class="form-line__item">
        <div>Заказчик</div>
        <div v-if="client.length < 1" @click="clientModal = true">
          <base-button>Добавить</base-button>
        </div>
        <div v-else class="selected-item">{{ client.name }}<span @click="removeClient">X</span></div>
      </div>
      <div class="form-line__item">
        <div>Поставщик</div>
        <div v-if="company.length < 1" @click="companyModal = true">
          <base-button>Добавить</base-button>
        </div>
        <div v-else class="selected-item">{{ company.name }}<span @click="removeCompany">X</span></div>
      </div>
    </div>

    <!-- Указание количество дней поставки и оплаты -->
    <div class="form-line">
      <div class="form-line__item">
        <label for="delivery-days">Дней на поставку</label>
        <input id="delivery-days" name="delivery-days" type="text" ref="deliveryDaysInput">
      </div>
      <div class="form-line__item">
        <label for="pay-days">Дней на оплату</label>
        <input id="pay-days" name="pay-days" type="text" ref="payDaysInput">
      </div>
    </div>

    <!-- Указание цены и выбор региона -->
    <div class="form-line">
      <div class="form-line__item">
        <label for="price">Стоимость</label>
        <input id="price" name="price" type="text" ref="priceInput">
      </div>
      <div class="form-line__item">
        <div>Регион</div>
        <div v-if="region.length < 1" @click="regionModal = true">
          <base-button>Добавить</base-button>
        </div>
        <div v-else class="selected-item">{{ region.name }}<span @click="removeRegion">X</span></div>
      </div>
    </div>

    <!-- Выбор товаров и признака исполнения -->
    <div class="form-line">
      <div class="form-line__item">
        <div>Товары</div>
        <div v-if="products.length < 1" @click="productsModal = true">
          <base-button>Добавить</base-button>
        </div>
        <div v-else>
          <div class="selected-item" v-for="product in products" :key="product.id">{{ product.product.name }}<span
              @click="removeOneProduct(product)">X</span>
          </div>
          <base-button @click="removeProducts">Удалить все</base-button>
        </div>
      </div>
      <div class="form-line__item">
        <div>Признак выполнения <span>(не обязательно)</span></div>
        <div class="checkbox">
          <label for="done">Выполнен</label>
          <input type="checkbox" name="done" ref="Done">
        </div>
      </div>
    </div>

    <div class="form-line">
      <base-button type="submit" mode="submit">Создать</base-button>
    </div>

  </form>

  <company-modal v-show="companyModal" @close-modal="companyModal = false"></company-modal>
  <client-modal v-show="clientModal" @close-modal="clientModal = false"></client-modal>
  <region-modal v-show="regionModal" @close-modal="regionModal = false"></region-modal>
  <products-modal v-show="productsModal" @close-modal="productsModal = false"></products-modal>

</template>

<script>
import { serverUrl } from '../../config.js';
import BaseButton from '../UI/BaseButton.vue';
import ClientModal from "../UI/ClientModal.vue";
import CompanyModal from "../UI/CompanyModal.vue";
import ProductsModal from "../UI/ProductsModal.vue";
import RegionModal from "../UI/RegionModal.vue";

export default {
  data() {
    return {
      companyModal: false,
      clientModal: false,
      productsModal: false,
      regionModal: false,
    };
  },

  computed: {
    company() {
      return this.$store.getters['comps/company'];
    },
    client() {
      return this.$store.getters['clients/client'];
    },
    region() {
      return this.$store.getters['regions/region'];
    },
    products() {
      return this.$store.getters['prods/getProductsFromInput'];
    }
  },

  methods: {
    removeCompany() {
      this.$store.commit('comps/removeCompany');
    },
    removeClient() {
      this.$store.commit('clients/removeClient');
    },
    removeRegion() {
      this.$store.commit('regions/removeRegion');
    },
    removeProducts() {
      this.$store.commit('prods/removeProducts');
    },
    removeOneProduct(product) {
      const productIndex = this
        .$store
        .getters['prods/getProductsFromInput']
        .findIndex((item) => item.product.id === product.product.id);
      this.$store.commit('prods/removeProduct', productIndex);
    },
    submitData() {
      const contract = {
        number: this.$refs.numberInput.value,
        notice_number: this.$refs.noticeNumberInput.value,
        start_date: this.$refs.startDateInput.value,
        end_date: this.$refs.endDateInput.value.length > 0
          ? this.$refs.endDateInput.value
          : null,
        price: +this.$refs.priceInput.value,
        is_done: this.$refs.Done.checked,
        days_to_deliver: +this.$refs.deliveryDaysInput.value,
        days_to_pay: +this.$refs.payDaysInput.value,
        client: this.$store.getters['clients/client'].id,
        company: this.$store.getters['comps/company'].id,
        region: this.$store.getters['regions/region'].id,
        products: [...this.$store.getters['prods/getProductsIds']],
        user: +this.$store.getters['users/getId']
      };

      fetch(`${ serverUrl }/api/v1/contract/create`, {
        method: 'POST',
        body: JSON.stringify(contract),
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `JWT ${ this.$store.getters['users/getToken'] }`
        }
      });

      this.$router.push('/');
    }
  },

  components: { BaseButton, ClientModal, CompanyModal, ProductsModal, RegionModal },
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

button,
.checkbox {
  margin: 5px;
  padding: 5px;
}

form {
  display: flex;
  flex-direction: column;
}

label>span,
div>span {
  font-size: 0.7rem;
  font-style: italic;
}

.selected-item {
  margin: 5px;
  padding: 5px;
  color: #1d3557;
}

.selected-item>span {
  margin-left: 5px;
  font-weight: bold;
  color: #E63946;
  cursor: pointer;
}

.form-line {
  display: flex;
  justify-content: center;
}

.form-line__item {
  display: flex;
  flex-direction: column;
  width: 23.5rem;
  padding: 1rem;
}
</style>