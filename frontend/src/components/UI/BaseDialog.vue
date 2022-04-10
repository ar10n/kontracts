<template>
  <div class="background"></div>
  <dialog open>
    <header>
      <div>Контракт №{{ contractInfo.number }}</div>
      <div>{{ contractInfo.company.name }}</div>
    </header>
    <section>
      <div class="client">Заказчик: {{ contractInfo.client.name }} ({{ contractInfo.region.name }})</div>
      <div>Телефон: {{ contractInfo.client.phone }}</div>
      <div>ИНН: {{ contractInfo.client.inn }}</div>
      <div>Email: {{ contractInfo.client.email }}</div>
      <hr>
      <div>Дата подписания: {{ contractInfo.start_date }}</div>
      <div>Срок действия: до {{ contractInfo.end_date }}</div>
      <hr>
      <div class="price">Цена контракта: {{ contractInfo.price }} руб.</div>
    </section>
    <menu>
      <slot name="actions"></slot>
    </menu></dialog>
</template>

<script>
export default {
  props: ['contractInfo'],
}
</script>

<style scoped>
.client,
.price {
  font-size: 1.2rem;
  font-weight: 800;
}

.price {
  color: #1D3557;
}

.background {
  position: fixed;
  top: 0;
  left: 0;
  height: 100vh;
  width: 100%;
  background-color: rgba(0, 0, 0, 0.55);
  z-index: 10;
}

dialog {
  position: fixed;
  top: 10vh;
  left: 20%;
  right: 20%;
  width: 60%;
  z-index: 100;
  border-radius: 5px;
  border: none;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
  padding: 0;
  margin: 0;
  overflow: hidden;
}

header {
  background-color: #1D3557;
  color: #F1FAEE;
  width: 100%;
  padding-top: 1rem;
  padding-bottom: 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

header>div {
  padding-right: 1.5rem;
  padding-left: 1.5rem;
  font-size: 1.5rem;
}

section {
  padding: 1rem;
}

section>div {
  padding: 0.5rem;
}

menu {
  padding: 1.5rem;
  display: flex;
  justify-content: flex-end;
  margin: 0;
}
</style>