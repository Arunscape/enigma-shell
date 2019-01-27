<template>
  <div id="app">
    <Editor/>
    <!-- <codemirror/> -->
  </div>
</template>

<script>
import Editor from "./components/Editor.vue";
import { codemirror } from "vue-codemirror";
import "codemirror/lib/codemirror.css";

// you can set default global options and events when use
Vue.use({
  VueCodemirror,
  options: { theme: "base16-dark" },
  events: ["scroll"]
});

export default {
  name: "app",
  components: {
    Editor,
    codemirror
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
