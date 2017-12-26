// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import Autoscroll from 'vue-autoscroll'
import Vuex from 'vuex'
import { ClientTable, Event } from 'vue-tables-2';
import VueNumeric from 'vue-numeric'
import VueCurrencyFilter from 'vue-currency-filter'

Vue.use(VueNumeric)
Vue.use(VueCurrencyFilter, {
    symbol: '원',
    thousandsSeparator: ',',
    // fractionCount: 3,
    // fractionSeparator: ',',
    symbolPosition: 'back',
    symbolSpacing: true
})

Vue.config.productionTip = false
Vue.use(Autoscroll)
Vue.use(ClientTable)
Vue.use(Vuex)
    /* eslint-disable no-new */
var vm = new Vue({
    el: '#app',
    template: '<App/>',
    components: { App }
})