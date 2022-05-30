export default {
  namespaced: true,
  state: {
    contracts: [],
    contract: [],
    contractDetails: {
      number: '',
      start_date: '',
      end_date: '',
      price: 0,
      client: {},
      company: {},
      region: {},
      products: {},
      claims: [
        {deadline: ''}
      ],
      shipments: [
        {
          delivery_date: {
            type: Date
          },
          pay_date: {
            type: Date
          },
          is_delivered: {
            type: Boolean
          },
          is_paid: {
            type: Boolean
          }
        },
      ],
      manufacturer: {},
      is_done: false,
      days_to_deliver: null,
      days_to_pay: null
    }
  },
  mutations: {
    addContracts(state, payload) {
      state.contracts = payload.contracts;
    },
    addContractDetails(state, payload) {
      state.contractDetails = payload.contract;
    },
    addContract(state, payload) {
      state.contract = payload.contract;
    },
    removeContract(state) {
      state.contract = [];
    }
  },
  getters: {
    contracts(state) {
      return state.contracts;
    },
    contract(state) {
      return state.contractDetails;
    },
    contractInClaim(state) {
      return state.contract;
    }
  },
  actions: {
    async addContracts(context, payload) {
      context.commit('addContracts', await payload);
    },
    async addContractDetails(context, payload) {
      context.commit('addContractDetails', await payload);
    },
    async addContract(context, payload) {
      context.commit('addContract', await payload);
    }
  }
};