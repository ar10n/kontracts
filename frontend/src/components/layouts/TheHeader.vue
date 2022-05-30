<template>
  <div>
    <header>
      <router-link to="/">
        KONTRACTS
      </router-link>

      <div class="buttons">
        <router-link to="/claims/create">
          Добавить претензию
        </router-link>
        <router-link to="/clients/create">
          Добавить клиента
        </router-link>
        <router-link to="/contracts/create">
          Добавить контракт
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

header > a {
  text-decoration: none;
  padding: 0.3rem;
  margin: 0.3rem;
  color: #f1faee;
}

.buttons > a {
  text-decoration: none;
  font-size: 0.8rem;
  padding: 0.3rem;
  margin: 0.3rem;
  border: 1px solid #f1faee;
  border-radius: 5px;
  background-color: #1d3557;
  color: #f1faee;
}

.buttons > a:hover {
  background-color: #f1faee;
  color: #1d3557;
  transition: all 300ms ease-out;
}

.buttons > .router-link-active {
  background-color: #f1faee;
  color: #1d3557;
  cursor: not-allowed;
}
</style>
