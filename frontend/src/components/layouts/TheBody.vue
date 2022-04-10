<template>
  <div class="body-container">
    <div class="content">
      <the-contracts></the-contracts>
    </div>
  </div>
</template>

<script>
import TheContracts from '../contracts/TheContracts.vue';

export default {
  components: {
    TheContracts,
  },
}
</script>

<style scoped>
.body-container {
  display: flex;
  flex-direction: column;
}
</style>