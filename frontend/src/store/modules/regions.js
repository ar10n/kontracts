export default {
  namespaced: true,
  state: {
    regions: [],
    region: []
  },
  mutations: {
    addRegions(state, payload) {
      state.regions = payload.regions;
    },
    addRegion(state, payload) {
      state.region = payload.region;
    },
    removeRegion(state) {
      state.region = [];
    }
  },
  getters: {
    regions(state) {
      return state.regions;
    },
    region(state) {
      return state.region;
    }
  },
  actions: {
    async addRegions(context, payload) {
      context.commit('addRegions', await payload);
    }
  }
};