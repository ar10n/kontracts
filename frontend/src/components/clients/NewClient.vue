<template>
  <h2>Новый клиент</h2>

  <form @submit.prevent="submitData">

    <div class="form-line">
      <div class="form-line__item first-line">
        <label for="name">Наименование</label>
        <input id="name" name="name" type="text" ref="nameInput">
      </div>
    </div>

    <div class="form-line">
      <div class="form-line__item second-line">
        <label for="phone">Телефон</label>
        <input id="phone" name="phone" type="text" ref="phoneInput">
      </div>
      <div class="form-line__item second-line">
        <label for="email">Email</label>
        <input id="email" name="email" type="email" ref="emailInput">
      </div>
      <div class="form-line__item second-line">
        <label for="inn">ИНН</label>
        <input id="inn" name="inn" type="text" ref="innInput">
      </div>
    </div>

    <div class="form-line">
      <div class="form-line__comment">
        <label for="comment">Комментарий</label>
        <textarea id="comment" name="comment" rows="5" ref="commentInput"></textarea>
      </div>
    </div>

    <div class="form-line">
      <div>
        <base-button type="submit" mode="submit">Создать</base-button>
      </div>
    </div>

  </form>

</template>

<script>
import { serverUrl } from '../../config.js';
import BaseButton from '../UI/BaseButton.vue';

export default {
  data() {
    return {
      clients: [],
      companies: [],
      regions: [],
      products: []
    };
  },
  components: { BaseButton },
  methods: {
    submitData() {
      const data = {
        'name': this.$refs.nameInput.value,
        'inn': this.$refs.innInput.value,
        'phone': this.$refs.phoneInput.value,
        'email': this.$refs.emailInput.value,
        'comment': this.$refs.commentInput.value
      };

      fetch(`${ serverUrl }/api/v1/client/create`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `JWT ${ this.$store.getters['users/getToken'] }`
        },
        body: JSON.stringify(data)
      });
    }
  },
};
</script>

<style scoped>
h2 {
  color: #1d3557;
  text-align: center;
}

input {
  font-family: inherit;
  margin: 5px;
  padding: 5px;
  border-radius: 5px;
  border: 1px solid #1d3557;
}

form {
  display: flex;
  flex-direction: column;
}


label>span,
div>span {
  font-size: 0.7rem;
  font-style: italic;
}

textarea {
  resize: none;
  margin: 5px;
  padding: 5px;
  border-radius: 5px;
  border: 1px solid #1d3557;
}

.form-line {
  display: flex;
  justify-content: center;
}

.form-line__item {
  display: flex;
  flex-direction: column;
  padding: 1rem;
}

.first-line {
  width: 49rem;
}

.second-line {
  width: 15rem;
}

.form-line__comment {
  display: flex;
  flex-direction: column;
  width: 49rem;
  padding: 1rem;
}

textarea {
  resize: none;
  margin: 5px;
  padding: 5px;
  border-radius: 5px;
  border: 1px solid #1d3557;
}
</style>