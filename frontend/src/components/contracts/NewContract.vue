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
        <label for="notice_number">Номер извещения</label>
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
        <label for="end_date">Срок действия</label>
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
              @click="removeProducts">X</span></div>
        </div>
      </div>
      <div class="form-line__item">
        <div>Признак выполнения</div>
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
      regionModal: false
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
      return this.$store.getters['regions/region']
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
    submitData() {
      const numberInput = this.$refs.numberInput.value;
      const noticeNumberInput = this.$refs.noticeNumberInput.value;
      const startDateInput = this.$refs.startDateInput.value;
      const endDateInput = this.$refs.endDateInput.value;
      const priceInput = this.$refs.priceInput.value;

      console.log(numberInput, noticeNumberInput, startDateInput, endDateInput, priceInput);
    }
  },

  components: {BaseButton, ClientModal, CompanyModal, ProductsModal, RegionModal},

  created() {
    fetch('http://127.0.0.1:8000/api/v1/product/list')
        .then(response => response.json())
        .then(data => this.products = data);
  },
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

button {
  margin: 5px;
  padding: 5px;
}

form {
  display: flex;
  flex-direction: column;
}

.selected-item {
  margin: 5px;
  padding: 5px;
  color: #1d3557;
}

.selected-item > span {
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
  width: 25%;
  padding: 1rem;
}

.radio-line {
  display: flex;
  justify-content: space-between;
  margin-top: 1rem;
}
</style>