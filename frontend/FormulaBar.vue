<template>
  <div id="formula-bar">
    <input v-model="formulaInput" placeholder="Enter formula" />
    <button @click="applyFormula">Apply</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      formulaInput: ''
    };
  },
  methods: {
    applyFormula() {
      this.$emit('applyFormula', this.formulaInput);
    }
  }
};
</script>

<style scoped>
#formula-bar {
  padding: 10px;
  background-color: #f1f1f1;
  display: flex;
  justify-content: space-between;
}
</style>
