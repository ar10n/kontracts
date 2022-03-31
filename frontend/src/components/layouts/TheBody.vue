<template>
  <div class="body-container">
    <div class="tab-panel">
      <TabButton @click="setSelectedTab('the-contracts')">Контракты</TabButton>
      <TabButton @click="setSelectedTab('the-claims')">Претензии</TabButton>
      <TabButton>Клиенты</TabButton>
      <TabButton>Товары</TabButton>
      <TabButton>Регионы</TabButton>
    </div>
    <div class="content">
      <component :is="selectedTab"></component>
    </div>
  </div>
</template>

<script>
import TheClaims from '../claims/TheClaims.vue';
import TheContracts from '../contracts/TheContracts.vue';
import TabButton from '../UI/TabButton.vue';

export default {
  data() {
    return {
      selectedTab: 'the-contracts'
    }
  },
  components: { TabButton, TheContracts, TheClaims },
  methods: {
    setSelectedTab(tab) {
      this.selectedTab = tab;
    }
  }
}
</script>

<style scoped>
.body-container {
  display: flex;
  flex-direction: column;
}
.tab-panel {
  display: flex;
  justify-content: space-around;
  align-items: flex-start;
  flex-direction: row;
  padding-top: 5px;
  padding-bottom: 5px;
}

.content {
  border-top: 1px dotted #1d3557;
}
</style>