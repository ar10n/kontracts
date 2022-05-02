import { createApp } from 'vue';
import { createRouter, createWebHistory } from 'vue-router';
import App from './App.vue';
import ContractDetails from './components/contracts/ContractDetails.vue';
import TheContracts from './components/contracts/TheContracts.vue';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/contracts', component: TheContracts },
    { path: '/contracts/:id', component: ContractDetails }
  ]
});
const app = createApp(App);

app.use(router);

app.mount('#app')
