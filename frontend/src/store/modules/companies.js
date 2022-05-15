export default {
  namespaced: true,
  state: {
    companies: [],
    company: []
  },
  mutations: {
    addCompanies(state, payload) {
      state.companies = payload.companies;
    },
    addCompany(state, payload) {
      state.company = payload.company;
    },
    removeCompany(state) {
      state.company = [];
    }
  },
  getters: {
    companies(state) {
      return state.companies;
    },
    company(state) {
      return state.company;
    }
  },
  actions: {
    async addCompanies(context, payload) {
      context.commit('addCompanies', await payload);
    }
  }
};