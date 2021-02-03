<template>
  <div class="container">
    <button type="button" class="btn btn-primary">{{msg}}</button>
    <p>{{msg}}</p>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: "Ping",
  data(){
    return {
      msg:'',
    };
  },
  methods:{
    //getMessage
    getMessage(){
      const path = 'http://localhost:5000/ping';
      axios.get(path)
          .then((res)=>{
            this.msg = res.data;
          }).catch((error)=>{
            console.error(error)
      });
    },
    //created()
    created(){
      this.getMessage();
    },


  }
}
</script>

<style scoped>

</style>