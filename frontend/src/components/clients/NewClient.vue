<template>

  <h2>Новый клиент</h2>

  <form @submit.prevent="submitData">

    <div class="form-line">
      <div class="form-line__item">
        <label for="name">Наименование</label>
        <input id="name" name="name" type="text" ref="nameInput">
      </div>
      <div class="form-line__item">
        <label for="inn">ИНН</label>
        <input id="inn" name="inn" type="text" ref="innInput">
      </div>
    </div>

    <div class="form-line">
      <div class="form-line__item">
        <label for="phone">Телефон</label>
        <input id="phone" name="phone" type="text" ref="phoneInput">
      </div>
      <div class="form-line__item">
        <label for="email">Email</label>
        <input id="email" name="email" type="email" ref="emailInput">
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
import BaseButton from '../UI/BaseButton.vue';

export default {
  data() {
    return {
      clients: [],
      companies: [],
      regions: [],
      products: []
    }
  },
  components: { BaseButton },
  methods: {
    submitData() {
      const nameInput = this.$refs.nameInput.value;
      const innInput = this.$refs.innInput.value;
      const phoneInput = this.$refs.phoneInput.value;
      const emailInput = this.$refs.emailInput.value;
      const commentInput = this.$refs.commentInput.value;

      const data = {
        'name': nameInput,
        'inn': innInput,
        'phone': phoneInput,
        'email': emailInput,
        'comment': commentInput
      };

      fetch('http://127.0.0.1:8000/api/v1/client/create', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      })
    }
  },
}
</script>

<style scoped>
h2 {
  color: #1d3557;
  text-align: center;
}

input {
  font-family: inherit;
}

form {
  display: flex;
  flex-direction: column;
}

textarea {
  resize: none;
}

.form-line {
  display: flex;
  justify-content: center;
}

.form-line__item {
  display: flex;
  flex-direction: column;
  width: 25%;
  padding: 1rem;
}

.form-line__comment {
  display: flex;
  flex-direction: column;
  width: calc(50% + 2rem);
  padding: 1rem;
}
</style>