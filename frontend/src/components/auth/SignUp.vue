<template>
  <h2>Регистрация</h2>

  <form @submit.prevent="submitData">
    <div class="form-line">
      <div class="form-line__item">
        <label for="login">Логин:</label>
        <input id="login" name="login" type="text" ref="loginInput">
      </div>
      <div class="form-line__item">
        <label for="email">Email:</label>
        <input id="email" name="email" type="email" ref="emailInput">
      </div>
    </div>
    <div class="form-line">
      <div class="form-line__item">
        <label for="firstPwd">Пароль:</label>
        <input id="firstPwd" name="firstPwd" type="password" ref="firstPwdInput">
      </div>
      <div class="form-line__item">
        <label for="secondPwd">Еще раз:</label>
        <input id="secondPwd" name="secondPwd" type="password" ref="secondPwdInput">
      </div>
    </div>
    <div class="form-line">
      <div class="form-line__item">
        <label for="firstName">Имя:</label>
        <input id="firstName" name="firstName" type="text" ref="firstNameInput">
      </div>
      <div class="form-line__item">
        <label for="secondName">Фамилия:</label>
        <input id="secondName" name="secondName" type="text" ref="secondNameInput">
      </div>
    </div>

    <div class="form-line">
      <base-button type="submit" mode="submit">Зарегистрироваться</base-button>
    </div>

    <div class="form-line">
      <div class="signup-text">Уже есть аккаунт?</div>
      <router-link class="signup-link" to="/signin">Войти</router-link>
    </div>
  </form>

  <pwd-modal v-show="pwdNotMatch" @close-modal="clearPwd"></pwd-modal>

</template>
<script>
import { serverUrl } from '../../config.js';
import BaseButton from '../UI/BaseButton.vue';
import PwdModal from '../UI/PwdModal.vue';

export default {
  data() {
    return {
      pwdNotMatch: false
    }
  },
  components: { BaseButton, PwdModal },
  methods: {
    clearPwd() {
      this.$refs.firstPwdInput.value = '';
      this.$refs.secondPwdInput.value = '';
      this.pwdNotMatch = false;
    },
    submitData() {
      const firstPwd = this.$refs.firstPwdInput.value;
      const secondPwd = this.$refs.secondPwdInput.value;

      if (firstPwd === secondPwd) {
        const newUser = {
          username: this.$refs.loginInput.value,
          password: firstPwd,
          email: this.$refs.emailInput.value,
          first_name: this.$refs.firstNameInput.value,
          last_name: this.$refs.secondNameInput.value
        }

        try {
          fetch(`${ serverUrl }/api/v1/auth/users/`, {
            method: 'POST',
            body: JSON.stringify(newUser),
            headers: {
              'Content-Type': 'application/json'
            }
          })
          this.$router.push('/signin');
        } catch (e) {
          console.log(e);
        }
      } else {
        this.pwdNotMatch = true;
      }
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