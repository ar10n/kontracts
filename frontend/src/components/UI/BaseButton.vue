<template>
  <button type="button" :class="mode">
    <slot></slot>
  </button>
</template>

<script>
export default {
  props: ['mode']
}
</script>

<style scoped>
button {
  border: none;
  border-radius: 5px;
  width: 150px;
  height: 30px;
  font-family: inherit;
  cursor: pointer;
}

.base {
  background-color: #E63946;
  color: #F1FAEE;
}

.submit {
  background-color: #1D3557;
  color: #F1FAEE;
}
</style>