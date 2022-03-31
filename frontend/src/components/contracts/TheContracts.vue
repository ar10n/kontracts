<template>
  <div class="contracts-table">
    <div class="contracts-table__headers">
      <div class="headers__item">Номер контракта</div>
      <div class="headers__item">Извещение</div>
      <div class="headers__item">Дата подписания</div>
      <div class="headers__item">Цена</div>
      <div class="headers__item">Клиент</div>
      <div class="headers__item">Поставщик</div>
      <div class="headers__item">Регион</div>
    </div>
  </div>
</template>

<style scoped>
.contracts-table {
  margin: 1%;
}

.contracts-table__headers {
  display: grid;
  grid-template-areas: "number notice start-date price client company region";
  grid-template-columns: 15% 15% 10% 15% 15% 15% 15%;
}

.headers__item {
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  font-weight: bold;
  font-size: 0.9rem;
  border-right: 1px solid #1d3557;
}

.headers__item:last-child {
  border-right: none;
}
</style>