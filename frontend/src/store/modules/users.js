export default {
  namespaced: true,
  state: {
    user: null,
    token: null,
    id: null,
  },
  mutations: {
    setUser(state, payload) {
      state.user = null;
      state.user = payload;
    },
    setToken(state, payload) {
      state.token = null;
      state.token = payload;
    },
    setId(state, payload) {
      state.id = null;
      state.id = payload;
    }
  },
  getters: {
    getUser(state) {
      return state.user;
    },
    getToken(state) {
      return state.token;
    },
    getId(state) {
      return state.id;
    }
  },
}