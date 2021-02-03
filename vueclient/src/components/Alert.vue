<template>
  <div>
    <b-alert varoamt="success" show>{{message}}</b-alert>
    <br>
  </div>
</template>

<script>
export default {
  name: "Alert",
  props:['message'],
};
</script>

<style scoped>

</style>