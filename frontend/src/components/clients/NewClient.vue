<template>
  <h2>Новый клиент</h2>

  <form @submit.prevent="submitData">
    <div>
      <label for="name">Наименование</label>
      <input id="name" name="name" type="text" ref="nameInput">
    </div>
    <div>
      <label for="inn">ИНН</label>
      <input id="inn" name="inn" type="text" ref="innInput">
    </div>
    <div>
      <label for="phone">Телефон</label>
      <input id="phone" name="phone" type="text" ref="phoneInput">
    </div>
    <div>
      <label for="email">Email</label>
      <input id="email" name="email" type="email" ref="emailInput">
    </div>
    <div>
      <label for="comment">Комментарий</label>
      <textarea id="comment" name="comment" rows="9" ref="commentInput"></textarea>
    </div>
    <div>
      <base-button type="submit" mode="submit">Создать</base-button>
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

.client-form {
  display: flex;
  justify-content: space-around;
}

.left-side {
  width: 45%;
}

.ls-element {
  display: flex;
  flex-direction: column;
  padding: 1rem;
}

.right-side {
  width: 45%;
  display: flex;
}

.radio-line {
  display: flex;
  justify-content: space-between;
  margin-top: 1rem;
}

.bold-label {
  font-weight: bold;
}

select,
input {
  font-family: inherit;
}

.form-line {
  display: flex;
  justify-content: space-around;
  margin-bottom: 0.5rem;
}

.line-element {
  display: flex;
  flex-direction: column;
  width: 45%;
}

.line-textarea {
  display: flex;
  flex-direction: column;
  width: 95%;
}

.line-textarea>textarea {
  resize: none;
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

.buttons {
  display: flex;
  justify-content: space-between;
}
</style>