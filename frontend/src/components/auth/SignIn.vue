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

    <div class="form-line">
      <div class="signup-text">Еще не зарегистрированы?</div>
      <router-link class="signup-link" to="/signup">Регистрация</router-link>
    </div>
  </form>
</template>
<script>
import BaseButton from '../UI/BaseButton.vue';

export default {
  components: { BaseButton },
  methods: {
    submitData() {
      const user = {
        username: this.$refs.loginInput.value,
        password: this.$refs.passwordInput.value
      }

      try {
        fetch('http://127.0.0.1:8000/api/v1/auth/jwt/create/', {
          method: 'POST',
          body: JSON.stringify(user),
          headers: {
            'Content-Type': 'application/json'
          }
        }).then(response => response.json()).then(data => {
          this.$store.commit('users/setUser', user.username);
          this.$store.commit('users/setToken', data.access);
          this.$router.push('/');
        })
      } catch (e) {
        console.log(e);
      }
    },
    setLogined(token) {
      console.log(token);
    }
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