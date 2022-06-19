<template>
  <div class="modal-overlay">
    <div class="modal">
      <h6>Добавление региона</h6>
      <input type="search" @input="regionFilter" ref="inputRegion" />
      <ul>
        <li v-for="region in filteredRegions" :key="region.id" @click="addRegion(region)">
          <span>{{ region.name }}</span>
        </li>
      </ul>
      <base-button @click="$emit('close-modal')">Закрыть</base-button>
    </div>
  </div>
</template>

<script>
import { serverUrl } from '../../config.js';
import BaseButton from "./BaseButton.vue";

export default {
  data() {
    return {
      filteredRegions: []
    };
  },
  created() {
    fetch(`${ serverUrl }/api/v1/region/list`, {
      method: 'GET',
      headers: {
        'Authorization': `JWT ${ this.$store.getters['users/getToken'] }`
      }
    })
      .then(response => response.json())
      .then(data => this.$store.dispatch('regions/addRegions', { regions: data }));
  },
  components: { BaseButton },
  methods: {
    // Фильтрация по названию региона
    regionFilter() {
      this.filteredRegions = [];
      const regions = this.$store.getters['regions/regions'];
      const inputRegion = this.$refs.inputRegion.value.toLowerCase();
      if (inputRegion.length > 0) {
        regions.filter(
          region => {
            if (region.name.toLowerCase().includes(inputRegion)) {
              this.filteredRegions.push(region);
            }
          }
        );
      } else {
        this.filteredRegions = [];
      }
    },
    // Добавление региона в форму + закрытие модала
    addRegion(region) {
      this.$store.commit('regions/addRegion', { region: region });
      this.$emit('close-modal');
    }
  }
};
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  display: flex;
  justify-content: center;
  background-color: #000000da;
}

.modal {
  text-align: center;
  background-color: white;
  height: 50%;
  width: 50%;
  margin-top: 10%;
  border-radius: 20px;
}

h6 {
  font-weight: 500;
  font-size: 28px;
}

input {
  font-family: inherit;
  margin: 5px;
  padding: 5px;
  border-radius: 5px;
  border: 1px solid #1d3557;
}

ul {
  padding: 0;
}

li {
  list-style-type: none;
  padding: 1%;
}

span:hover {
  color: #E63946;
  cursor: pointer;
  font-weight: bold;
}

button {
  background-color: #E63946;
  width: 150px;
  height: 40px;
  color: white;
  font-size: 14px;
  border-radius: 16px;
  margin-top: 50px;
}
</style>