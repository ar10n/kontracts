<template>
  <div class="modal-overlay">
    <div class="modal">
      <h6>Добавление товаров</h6>
      <input type="search" @input="productsFilter" ref="inputProduct" />
      <ul>
        <li v-for="product in filteredProducts" :key="product.id" @click="addProduct(product)">
          <span>{{ product.name }}</span>
        </li>
      </ul>
      <div v-if="selectedProducts.length > 0">
        <div class="selected-product" v-for="product in selectedProducts" :key="product.id">
          {{ product.product.name }} <span @click="removeFromSelected(product)">X</span>
        </div>
      </div>
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
      filteredProducts: []
    };
  },
  created() {
    fetch(`${ serverUrl }/api/v1/product/list`, {
      method: 'GET',
      headers: {
        'Authorization': `JWT ${ this.$store.getters['users/getToken'] }`
      }
    })
      .then(response => response.json())
      .then(data => this.$store.dispatch('prods/addProducts', { products: data }));
  },
  components: { BaseButton },
  computed: {
    selectedProducts() {
      return this.$store.getters['prods/getProductsFromInput'];
    }
  },
  methods: {
    // Фильтрация по названию
    productsFilter() {
      this.filteredProducts = [];
      const products = this.$store.getters['prods/products'];
      const inputProduct = this.$refs.inputProduct.value.toLowerCase();
      if (inputProduct.length > 0) {
        products.filter(
          product => {
            if (product.name.toLowerCase().includes(inputProduct)) {
              this.filteredProducts.push(product);
            }
          }
        );
      } else {
        this.filteredProducts = [];
      }
    },
    // Добавление в список продуктов и форму
    addProduct(product) {
      this.$store.commit('prods/addProduct', { product: product });
      this.filteredProducts = [];
      this.$refs.inputProduct.value = '';
    },
    // Удаление из списка продуктов и формы
    removeFromSelected(product) {
      const productIndex = this
        .$store
        .getters['prods/getProductsFromInput']
        .findIndex((item) => item.product.id === product.product.id);
      this.$store.commit('prods/removeProduct', productIndex);
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

.selected-product {
  color: #457B9D;
  font-style: italic;
}
</style>