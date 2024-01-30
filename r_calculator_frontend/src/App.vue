<template>
  <div id="app">
    <header>
      <h1 class="text-center">{{ $t('header.title') }}</h1>
    </header>


    <main class="container mt-4 text-center">
      <form @submit.prevent="calculate" class="mt-4">

        <div class="language-switch">
          <button class="language-button" @click="switchToFrance">Switch to France</button>
          <button class="language-button" @click="switchToEnglish">Switch to English</button>
          <button class="language-button" @click="switchToGerman">Switch to German</button>
        </div>

        <div class="form-group border">
          <label for="calculationType" class="text-black">{{ $t('form.calculationType') }}</label>
          <select v-model="calculationType" class="form-control custom-select">
            <option value="series">{{ $t('form.series') }}</option>
            <option value="parallel">{{ $t('form.parallel') }}</option>
          </select>
          
          <label for="resistances" class="text-black">{{ $t('form.resistances') }}</label>
          <div v-for="(resistance, index) in resistancesArray" :key="index">
            <input v-model="resistancesArray[index]" type="text" class="form-control" required>
            <button @click="removeResistance(index)" type="button" class="btn btn-danger btn-sm">-</button>
          </div>
          <button @click="addResistance" type="button" class="btn btn-success btn-sm">+</button>
          
          <button type="submit" class="btn btn-primary btn-beautiful">{{ $t('form.calculateButton') }}</button>
        </div>
      </form>

      <div v-if="result !== null" class="form-group">
        <p class="text-black result-text">{{ $t('result.label') }}: {{ result }} {{ $t('result.unit') }}</p>
      </div>

      <footer>
        <p>&copy; 2024 HTL-Weiz.</p>
      </footer>

    </main>
  </div>
</template>

<script>
export default {
  data() {
    return {
      calculationType: 'series',
      resistancesArray: [''], 
      result: null,
    };
  },
  methods: {
    calculate() {
      const resistancesArray = this.resistancesArray.map(value => parseFloat(value));
      const data = {
        calculation_type: this.calculationType,
        resistances: resistancesArray,
      };

      fetch('http://localhost:5000/calculate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      })
        .then(response => response.json())
        .then(data => {
          this.result = data.result;
        })
        .catch(error => {
          console.error('Error:', error);
        });
    },
    addResistance() {
      this.resistancesArray.push('');
    },
    removeResistance(index) {
      this.resistancesArray.splice(index, 1);
    },
    switchToEnglish() {
      this.$i18n.locale = 'en'; 
    },
    switchToGerman() {
      this.$i18n.locale = 'de'; 
    },
    switchToFrance(){
      this.$i18n.locale = 'fr';
    },
  },
};
</script>

<style>
body {
  font-family: 'Arial', sans-serif;
}

#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.bg-white {
  background-color: white;
}

.border {
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px;
}

.text-black {
  color: black;
}

.text-info {
  color: black;
  font-size: 12px;
}

.text-center {
  text-align: center;
}

.form-group {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  margin-top: 140px;
}

.form-control {
  width: 20%;
  margin-bottom: 10px;
}

.btn-beautiful {
  background-color: #1ba373;
  border: none;
  color: white;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  cursor: pointer;
  border-radius: 5px;
}

.result-text {
  font-size: 18px;
  font-weight: bold;
  color: black;
  margin-top: -100px;
}

.language-switch {
  position: absolute;
  top: 120px; 
  right: 20px; 
  display: flex;
  align-items: center;
}

.language-button {
  background-color: #1ba373;
  border: none;
  color: white;
  padding: 2px 10px;
  margin-left: 5px;
  cursor: pointer;
  border-radius: 3px;
  font-size: 14px;
}

header {
  background-color: #01284f;
  color: white;
  text-align: center;
  left: 0;
  right: 0;
  margin: 0;
  top: 0;
  position: fixed;
}

footer {
  background-color: #01284f;
  color: white;
  padding: 10px;
  text-align: center;
  position: fixed;
  bottom: 0;
  left: 0; 
  right: 0;
  margin: 0; 
}


@media (max-width: 576px) {
  #app {
    padding: 15px;
  }

  main{
    padding: 15px;
    text-align: center;
  }

  .language-switch {
    position: static;
    margin-top: 90px;
  }
}
</style>