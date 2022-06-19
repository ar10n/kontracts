<template>
  <h2>Вход</h2>

  <form @submit.prevent="submitData">
    <div class="form-line">
      <div class="form-line__item">
        <label for="login">Логин:</label>
        <input id="login" name="login" type="text" ref="loginInput">
      </div>
    </div>
    <div class="form-line">
      <div class="form-line__item">
        <label for="password">Пароль:</label>
        <input id="password" name="password" type="password" ref="passwordInput">
      </div>
    </div>

    <div class="form-line">
      <base-button type="submit" mode="submit">Войти</base-button>
    </div>

    <!-- <div class="form-line">
      <div class="signup-text">Еще не зарегистрированы?</div>
      <router-link class="signup-link" to="/signup">Регистрация</router-link>
    </div> -->
  </form>
</template>
<script>
import { serverUrl } from '../../config.js';
import BaseButton from '../UI/BaseButton.vue';

export default {
  components: { BaseButton },
  methods: {
    async submitData() {
      const user = {
        username: this.$refs.loginInput.value,
        password: this.$refs.passwordInput.value
      }

      await fetch(`${ serverUrl }/api/v1/auth/jwt/create/`, {
        method: 'POST',
        body: JSON.stringify(user),
        headers: {
          'Content-Type': 'application/json'
        }
      }).then(async response => response.json()).then(async data => {
        this.$store.commit('users/setUser', user.username);
        this.$store.commit('users/setToken', data.access);
      })

      await fetch(`${ serverUrl }/api/v1/auth/users/me`, {
        method: 'GET',
        headers: {
          'Authorization': `JWT ${ this.$store.getters['users/getToken'] }`
        }
      }).then(async response => response.json()).then(async data =>
        this.$store.commit('users/setId', data.id));

      this.$router.push('/');
    },
  }
}
</script>
<style scoped>
h2 {
  color: #1d3557;
  text-align: center;
}

form {
  display: flex;
  flex-direction: column;
  padding: 2rem;
}

.form-line {
  display: flex;
  justify-content: center;
  padding: 1rem;

}

.form-line__item {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

input {
  font-family: inherit;
  margin: 5px;
  padding: 5px;
  border-radius: 5px;
  border: 1px solid #1d3557;
}

.signup-text,
.signup-link {
  font-size: 0.8rem;
  padding: 0.2rem;
}
</style>