export default {
  namespaced: true,
  state: {
    products: [],
    productsFromInput: [],
    productsIds: []
  },
  mutations: {
    addProducts(state, payload) {
      state.products = payload.products;
    },
    addProduct(state, payload) {
      state.productsFromInput.push(payload);
    },
    removeProducts(state) {
      state.productsFromInput = [];
    },
    removeProduct(state, payload) {
      state.productsFromInput.splice(payload, 1);
    }
  },
  getters: {
    products(state) {
      return state.products;
    },
    getProductsFromInput(state) {
      return state.productsFromInput;
    },
    getProductsIds(state) {
      state.productsIds = [];
      state.productsFromInput.forEach(item => state.productsIds.push(item.product.id));
      return state.productsIds;
    }
  },
  actions: {
    async addProducts(context, payload) {
      context.commit('addProducts', await payload);
    }
  }
};