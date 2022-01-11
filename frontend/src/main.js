import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from '@/store/vuex'
import VeeValidate from 'vee-validate'
import vuetify from './plugins/vuetify'
import Dictionary from '@/assets/veeValidators'
import VueMask from 'v-mask'
Vue.use(VueMask);

Vue.config.productionTip = false


const veeValidateConfig = {
	inject: true,
	fieldsBagName: 'veeFields',
	errorBagName: 'veeErrors',
	classes: true,
	classNames: {
		valid: 'is-valid',
		invalid: 'is-invalid'
	},
	locale:'pt',
  dictionary: Dictionary
}

Vue.use(VeeValidate, veeValidateConfig)

Vue.filter('formatarData',function(val){
	return new Date(val).toLocaleString()
})

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
