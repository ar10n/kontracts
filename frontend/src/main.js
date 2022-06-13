import { createApp } from 'vue';
import { createRouter, createWebHistory } from 'vue-router';

import store from './store/index.js';

import App from './App.vue';
import SignIn from './components/auth/SignIn.vue';
import SignUp from './components/auth/SignUp.vue';
import NewClaim from './components/claims/NewClaim.vue';
import NewClient from './components/clients/NewClient.vue';
import ContractDetails from './components/contracts/ContractDetails.vue';
import NewContract from './components/contracts/NewContract.vue';
import TheContracts from './components/contracts/TheContracts.vue';
import NewShipment from './components/shipments/NewShipment.vue';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: TheContracts },
    { path: '/claims/create', component: NewClaim },
    { path: '/clients/create', component: NewClient },
    { path: '/contracts/create', component: NewContract },
    { path: '/contracts/:id', component: ContractDetails },
    { path: '/shipments/create', component: NewShipment },
    { path: '/signin', component: SignIn },
    { path: '/signup', component: SignUp }
  ]
});

const app = createApp(App);

app.use(router);
app.use(store);

app.mount('#app');
