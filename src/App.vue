<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/logo.png" /> -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js App" /> -->
    <div id="vert-split">
      <div><Documentation /></div>
      <div><Editor /></div>
      <div>1</div>
      <div>2</div>
    </div>
  </div>
</template>

<script>
//import HelloWorld from "./components/HelloWorld.vue";
import Editor from "./components/Editor.vue";
import Documentation from "./components/Documentation.vue";

export default {
  name: "app",
  components: {
//    HelloWorld,
    Editor,
    Documentation
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
  /* margin-top: 60px; */
}
</style>
