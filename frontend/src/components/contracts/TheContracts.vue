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
    <div class="contracts-table__body">
      <div class="body-line">
        <div class="body-line__item">123</div>
        <div class="body-line__item">0123456789</div>
        <div class="body-line__item">02.04.2022</div>
        <div class="body-line__item">100000.00</div>
        <div class="body-line__item">ГКБ</div>
        <div class="body-line__item">Лекопт</div>
        <div class="body-line__item">Москва</div>
      </div>
      <div class="body-line">
        <div class="body-line__item">123</div>
        <div class="body-line__item">0123456789</div>
        <div class="body-line__item">02.04.2022</div>
        <div class="body-line__item">100000.00</div>
        <div class="body-line__item">ГКБ</div>
        <div class="body-line__item">Лекопт</div>
        <div class="body-line__item">Москва</div>
      </div>
      <div class="body-line">
        <div class="body-line__item">123</div>
        <div class="body-line__item">0123456789</div>
        <div class="body-line__item">02.04.2022</div>
        <div class="body-line__item">100000.00</div>
        <div class="body-line__item">ГКБ</div>
        <div class="body-line__item">Лекопт</div>
        <div class="body-line__item">Москва</div>
      </div>
      <div class="body-line">
        <div class="body-line__item">123</div>
        <div class="body-line__item">0123456789</div>
        <div class="body-line__item">02.04.2022</div>
        <div class="body-line__item">100000.00</div>
        <div class="body-line__item">ГКБ</div>
        <div class="body-line__item">Лекопт</div>
        <div class="body-line__item">Москва</div>
      </div>
      <div class="body-line">
        <div class="body-line__item">123</div>
        <div class="body-line__item">0123456789</div>
        <div class="body-line__item">02.04.2022</div>
        <div class="body-line__item">100000.00</div>
        <div class="body-line__item">ГКБ</div>
        <div class="body-line__item">Лекопт</div>
        <div class="body-line__item">Москва</div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.contracts-table {
  margin: 1%;
}

.contracts-table__headers,
.body-line {
  display: grid;
  grid-template-areas: "number notice start-date price client company region";
  grid-template-columns: 15% 15% 10% 15% 25% 10% 10%;
  padding-top: 1%;
  padding-bottom: 1%;
  cursor: default;
}

.contracts-table__headers {
  border-bottom: 1px solid #1d3557;
}

.headers__item {
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  font-weight: 500;
  border-right: 1px solid #1d3557;
}

.headers__item:last-child,
.body-line__item:last-child {
  border-right: none;
}

.body-line {
  border-radius: 10px;
}

.body-line:hover {
  background-color: #f1faee;
  border-radius: 10px;
}

.body-line:hover > .body-line__item {
  border-right: 1px solid #1d3557;
}

.body-line:hover > .body-line__item:last-child {
  border-right: none;
}

.body-line__item {
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  border-right: 1px solid #1d3557;
  font-size: 0.9rem;
}
</style>