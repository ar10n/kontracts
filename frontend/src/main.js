import { createApp } from 'vue';
import { createRouter, createWebHistory } from 'vue-router';
import App from './App.vue';
import NewClient from './components/clients/NewClient.vue';
import ContractDetails from './components/contracts/ContractDetails.vue';
import TheContracts from './components/contracts/TheContracts.vue';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/clients/create', component: NewClient },
    { path: '/', component: TheContracts },
    { path: '/contracts/create', component: TheContracts },
    { path: '/contracts/:id', component: ContractDetails }
  ]
});
const app = createApp(App);

app.use(router);

app.mount('#app')
