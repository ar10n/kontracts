<template>
  <div>
    <header>
      <div class="logo">KONTRACTS</div>
      <router-link to="/">
        Все контракты
      </router-link>

      <div class="buttons">
        <router-link to="/clients/create">
          Новый клиент
        </router-link>
        <router-link to="/contracts/create">
          Новый контракт
        </router-link>
      </div>
    </header>
  </div>
</template>

<style scoped>
header {
  background-color: #1d3557;
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 5vh;
}

a {
  text-decoration: none;
  padding: 0.3rem;
  margin: 0.3rem;
  border: 1px solid #f1faee;
  border-radius: 5px;
  background-color: #1d3557;
  color: #f1faee;
}

a:hover {
  background-color: #f1faee;
  color: #1d3557;
  transition: all 300ms ease-out;
}

.router-link-active {
  background-color: #f1faee;
  color: #1d3557;
  cursor: not-allowed;
}

.logo {
  color: #f1faee;
  font-size: 1.5rem;
  padding-left: 10px;
  cursor: default;
}
</style>
