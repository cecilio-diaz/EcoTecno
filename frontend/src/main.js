import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify';

Vue.config.productionTip = false

import * as VueGoogleMaps from 'vue2-google-maps';

import axios from 'axios'
import VueAxios from 'vue-axios'
axios.defaults.baseURL = 'http://90.147.184.214/api/v1/'

Vue.use(VueAxios, axios)

Vue.use(VueGoogleMaps, {
  load: {
    key: '$VUE_APP_MAPS_KEY',
    libraries: 'places'
  },
  installComponents: true
})

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')


