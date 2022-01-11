import Vue from 'vue'
import Vuex from 'vuex'
import RelatorioService from '@/services/RelatorioService'

Vue.use(Vuex)

const RelatorioStore = new Vuex.Store({
  state: {
    loading: false,
    relatorios: [],

  },
  mutations: {
    setLoading(state, value) { state.loading = value },
    
    setRelatorio(state, value) { state.relatorios = value },
  },
  getters:{ 
  },
  actions: {
    get_relatorios: async (context)=>{
      const req = new RelatorioService()
      context.commit('setLoading', true)
      return await req.listar()
      .then( response => { 
        context.commit('setRelatorio', response.data)
      }).catch( error => { 
        console.error(error.response); 
        context.commit('setRelatorio', [])
      }).finally( () => { 
        context.commit('setLoading', false) 
      })
    },
   
  }
})

export default RelatorioStore