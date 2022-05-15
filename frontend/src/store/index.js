import {createStore} from 'vuex';

import contractsModule from './modules/contracts.js';
import productsModule from './modules/products.js';
import regionsModule from './modules/regions.js';
import companiesModule from './modules/companies.js';
import clientsModule from './modules/clients.js';

const store = createStore({
  modules: {
    cons: contractsModule,
    prods: productsModule,
    regions: regionsModule,
    comps: companiesModule,
    clients: clientsModule
  }
});

export default store;