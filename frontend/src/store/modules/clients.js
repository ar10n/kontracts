export default {
  namespaced: true,
  state: {
    clients: [],
    client: []
  },
  mutations: {
    addClients(state, payload) {
      state.clients = payload.clients;
    },
    addClient(state, payload) {
      state.client = payload.client;
    },
    removeClient(state) {
      state.client = [];
    }
  },
  getters: {
    clients(state) {
      return state.clients;
    },
    client(state) {
      return state.client;
    }
  },
  actions: {
    async addClients(context, payload) {
      context.commit('addClients', await payload);
    }
  }
};