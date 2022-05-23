export default {
  namespaced: true,
  state: {
    contracts: [],
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