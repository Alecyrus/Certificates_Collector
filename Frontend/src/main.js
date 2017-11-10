// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import router from './router'

import App from './App.vue'
import axios from 'axios';
import VueLocalStorage from 'vue-ls';

import iView from 'iview';
import 'iview/dist/styles/iview.css';
import '../theme/index.less';
import VueParticles from 'vue-particles';
Vue.use(VueParticles)
Vue.use(iView);
Vue.prototype.$request = axios;
Vue.use(VueLocalStorage);
Vue.config.productionTip = false;
require('vue2-animate/dist/vue2-animate.min.css');
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
