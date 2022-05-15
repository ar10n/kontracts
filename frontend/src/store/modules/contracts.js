export default {
  namespaced: true,
  state: {
    contracts: [],
    contractDetails: {
      client: {},
      company: {},
      region: {},
      products: {},
      claims: {}
    }
  },
  mutations: {
    addContracts(state, payload) {
      state.contracts = payload.contracts;
    },
    addContractDetails(state, payload) {
      state.contractDetails = payload.contract;
    }
  },
  getters: {
    contracts(state) {
      return state.contracts;
    },
    contract(state) {
      return state.contractDetails;
    }
  },
  actions: {
    async addContracts(context, payload) {
      context.commit('addContracts', await payload);
    },
    async addContractDetails(context, payload) {
      context.commit('addContractDetails', await payload);
    }
  }
};