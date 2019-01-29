<template>
  <!-- bidirectional data binding（双向数据绑定） -->
  <!-- <codemirror v-model="code" :options="cmOptions"></codemirror> -->

  <!-- or to manually control the datasynchronization（或者手动控制数据流，需要像这样手动监听changed事件） -->
  <codemirror
    ref="myCm"
    :value="code"
    :options="cmOptions"
    @ready="onCmReady"
    @focus="onCmFocus"
    @input="onCmCodeChange"
  >
  </codemirror>

  <!-- if Nust.js/SSR（如果在 Nuxt.js 环境下，需要外面包裹一层 no-ssr） -->
  <!-- <no-ssr placeholder="Codemirror Loading...">
    <codemirror ref="myCm"
                :value="code"
                :options="cmOptions"
                @ready="onCmReady"
                @focus="onCmFocus"
                @input="onCmCodeChange">
    </codemirror>
  </no-ssr> -->
</template>

<script>
// language js
import "codemirror/mode/gas/gas.js";
// import "codemirror/mode/javascript/javascript.js";
// theme css
import "codemirror/theme/base16-dark.css";
// more codemirror resources
// import 'codemirror/some-resource...'

// require component
import { codemirror } from "vue-codemirror";

// require styles
import "codemirror/lib/codemirror.css";
import SimpleStore from "../SimpleStore.js";

export default {
  components: {
    codemirror
  },
  data() {
    return {
      code: SimpleStore.data.code,
      cmOptions: {
        // codemirror options
        tabSize: 4,
        mode: "text/x-gas",
        theme: "base16-dark",
        lineNumbers: true,
        line: true
        // more codemirror options, 更多 codemirror 的高级配置...
      }
    };
  },
  methods: {
    onCmReady(cm) {
      console.log("the editor is readied!", cm);
    },
    onCmFocus(cm) {
      console.log("the editor is focus!", cm);
    },
    onCmCodeChange(newCode) {
      console.log("this is new code", newCode);
      this.code = newCode;
      SimpleStore.data.code = newCode;
    }
  },
  computed: {
    codemirror() {
      return this.$refs.myCm.codemirror;
    }
  },
  mounted() {
    console.log("this is current codemirror object", this.codemirror);
    // you can use this.codemirror to do something...
  }
};
</script>

<style>
.CodeMirror {
  text-align: left !important;
  height: 50vh !important;
}
</style>
