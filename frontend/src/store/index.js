import { createStore } from 'vuex';

import clientsModule from './modules/clients.js';
import companiesModule from './modules/companies.js';
import contractsModule from './modules/contracts.js';
import productsModule from './modules/products.js';
import regionsModule from './modules/regions.js';
import userModule from './modules/users.js';

const store = createStore({
  modules: {
    cons: contractsModule,
    prods: productsModule,
    regions: regionsModule,
    comps: companiesModule,
    clients: clientsModule,
    users: userModule
  }
});

export default store;