<template>
  <h2>Новая претензия</h2>

  <form @submit.prevent="submitData">

    <div class="form-line">
      <div class="form-line__item second-line">
        <label for="name">Краткое описание</label>
        <input id="name" name="name" type="text" ref="nameInput">
      </div>
      <div class="form-line__item second-line">
        <div>Контракт</div>
        <div v-if="contract.length < 1" @click="contractModal = true">
          <base-button>Добавить</base-button>
        </div>
        <div v-else class="selected-item">{{ contract.number }}<span @click="removeContract">X</span></div>
      </div>
    </div>

    <div class="form-line">
      <div class="form-line__item second-line">
        <label for="start-date">Дата начала</label>
        <input id="start-date" name="start-date" type="date" ref="startDateInput">
      </div>
      <div class="form-line__item second-line">
        <label for="end-date">Дата окончания</label>
        <input id="end-date" name="end-date" type="date" ref="endDateInput">
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

  <contract-modal v-show="contractModal" @close-modal="contractModal = false"></contract-modal>

</template>

<script>
import { serverUrl } from '../../config.js';
import BaseButton from '../UI/BaseButton.vue';
import ContractModal from "../UI/ContractModal.vue";

export default {
  data() {
    return {
      contractModal: false
    }
  },
  name: "NewClaim",
  components: { BaseButton, ContractModal },
  computed: {
    contract() {
      return this.$store.getters['cons/contractInClaim'];
    }
  },
  methods: {
    submitData() {
      const data = {
        'name': this.$refs.nameInput.value,
        'start_date': this.$refs.startDateInput.value,
        'deadline': this.$refs.endDateInput.value,
        'comment': this.$refs.commentInput.value,
        'contract': this.$store.getters['cons/contractInClaim'].id
      };

      try {
        fetch(`${ serverUrl }/api/v1/claim/create`, {
          method: 'POST',
          body: JSON.stringify(data),
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `JWT ${ this.$store.getters['users/getToken'] }`
          }
        });
        this.$store.commit('cons/removeContract');
      } catch (e) {
        console.log(e);
      }
    },
    removeContract() {
      this.$store.commit('cons/removeContract');
    }
  }
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

.form-line {
  display: flex;
  justify-content: center;
}

.first-line {
  width: 49rem;
}

.second-line {
  width: 23.5rem;
}

.form-line__item {
  display: flex;
  flex-direction: column;
  padding: 1rem;
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

.selected-item>span {
  margin-left: 5px;
  font-weight: bold;
  color: #E63946;
  cursor: pointer;
}
</style>