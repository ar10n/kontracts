export default {
  namespaced: true,
  state: {
    products: []
  },
  mutations: {
    addProducts(state, payload) {
      state.products = payload.products;
    }
  },
  getters: {
    products(state) {
      return state.products;
    }
  },
  actions: {
    async addProducts(context, payload) {
      context.commit('addProducts', await payload);
    }
  }
};