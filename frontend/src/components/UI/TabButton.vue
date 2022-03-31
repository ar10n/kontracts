<template>
  <button class="tab-btn">
    <slot></slot>
  </button>
</template>

<style scoped>
.tab-btn {
  font-family: inherit;
  cursor: pointer;
  border: none;
  width: 8rem;
  height: 2rem;
  background-color: inherit;
  color: #1d3557;
  border-radius: 10px;
  transition: all 200ms ease-out;
}

.tab-btn:hover {
  border-radius: 10px;
  cursor: pointer;
  color: #f1faee;
  background-color: #1d3557;
  transition: all 200ms ease-out;
}
</style>