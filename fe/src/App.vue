<template>
  <div id="app">
    <h1>Chatty</h1>

    <table style="width: 25%; margin: auto; height: 300px">
        <tr v-for="(msg, index) in msgs" :key="index" >
          <td>
            {{msg}}
          </td>
        </tr>
    </table>
    <br/>
    <input 
          type="text" 
          class="form-control"  
          style="width: 25%; margin: auto;" 
          id="iname"  
          placeholder="your name here"
          v-model="iname"
    >
    <br/>
    <div class="form-group purple-border" style="width: 25%; margin: auto;">
      <textarea 
          class="form-control" 
          id="imsg" 
          rows="2"  
          placeholder="your message here, enter to send" 
          v-model="imsg"
          @keyup.enter="sendMessage">
      </textarea>
    </div>
  </div>
</template>

<script>
import axios from "axios";
const baseUrl = "http://localhost:5000";
export default {
  name: 'ChatBot',
  data(){
    return {
      msgs: [],
      imsg: '',
      iname: '',
    };
  },
  methods: {
    getData(){
      axios.get(baseUrl).then(res => this.msgs = res.data.data);
    },
    poll(){
      this.polling = setInterval (()=>{
        this.getData();
      }, 1000);
    },
    sendMessage(){
       axios.post(baseUrl, {"data": this.omsg})
       .then(() => {
         this.imsg = '';
         this.getData();
         });
    }
  },
  computed: {
      omsg(){  
        var user = this.iname 
        if (!user || 0 === user.length){
          user = 'anonymous'
        }
        return user + ": " + this.imsg;
      } 
  },
  beforeDestroy () {
    clearInterval(this.polling)
  },
  created(){
    this.poll();
  }
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
table {
 background-color: #fff;
}

tr {
  background-color: #42b983;
  color: rgb(21, 4, 255);
  text-align: left;
  vertical-align: text-top;
}

td {
  background-color: #f9f9f9;
}

tr, td {
  min-width: 120px;
  padding: 10px 20px;
}
</style>
