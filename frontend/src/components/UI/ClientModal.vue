<template>
  <div class="background"></div>
  <dialog open>
    <header>
      <div>Новый клиент</div>
    </header>
    <section>
      <form @submit.prevent="submitData">
        <div class="form-line">
          <div class="line-element">
            <label class="bold-label" for="name">Наименование</label>
            <input id="name" name="name" type="text" ref="nameInput">
          </div>
          <div class="line-element">
            <label class="bold-label" for="inn">ИНН</label>
            <input id="inn" name="inn" type="text" ref="innInput">
          </div>
        </div>
        <div class="form-line">
          <div class="line-element">
            <label class="bold-label" for="phone">Телефон</label>
            <input id="phone" name="phone" type="text" ref="phoneInput">
          </div>
          <div class="line-element">
            <label class="bold-label" for="email">Email</label>
            <input id="email" name="email" type="email" ref="emailInput">
          </div>
        </div>
        <div class="form-line">
          <div class="line-textarea">
            <label class="bold-label" for="comment">Комментарий</label>
            <textarea id="comment" name="comment" rows="5" ref="commentInput"></textarea>
          </div>
        </div>
        <menu class="buttons">
          <div>
            <base-button type="submit" mode="submit">Создать</base-button>
          </div>
          <slot name="actions"></slot>
        </menu>
      </form>
    </section>
  </dialog>
</template>

<script>
import BaseButton from './BaseButton.vue';

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

.buttons {
  display: flex;
  justify-content: space-between;
}
</style>