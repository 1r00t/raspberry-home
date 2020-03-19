import Vue from "vue";
import axios from "axios";
import VueAxios from "vue-axios";
import { BootstrapVue, BootstrapVueIcons } from "bootstrap-vue";

import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

import App from "./App.vue";
import router from "./router";

// import Line from "./components/Chart.vue"

Vue.use(BootstrapVue);
Vue.use(BootstrapVueIcons);
Vue.use(VueAxios, axios);

Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App),
  // components: {
  //   "Line": Line
  // }
}).$mount("#app");
