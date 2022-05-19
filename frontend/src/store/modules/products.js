export default {
  namespaced: true,
  state: {
    products: [],
    productsFromInput: []
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
    }
  },
  getters: {
    products(state) {
      return state.products;
    },
    getProductsFromInput(state) {
      return state.productsFromInput;
    }
  },
  actions: {
    async addProducts(context, payload) {
      context.commit('addProducts', await payload);
    }
  }
};