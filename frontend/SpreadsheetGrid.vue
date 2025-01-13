<template>
  <div id="spreadsheet">
    <hot-table :settings="hotSettings"></hot-table>
  </div>
</template>

<script>
import { HotTable } from '@handsontable/vue';

export default {
  components: {
    HotTable
  },
  data() {
    return {
      hotSettings: {
        data: [[]],  // Initialize with an empty grid
        colHeaders: true,
        rowHeaders: true,
        dropdownMenu: true,
        formulas: true,
        contextMenu: true
      }
    };
  }
};
</script>

<style scoped>
#spreadsheet {
  height: 500px;
  width: 100%;
}
</style>
