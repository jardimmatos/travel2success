import Vue from 'vue'
import Vuex from 'vuex'
import MovimentacaoService from '@/services/MovimentacaoService'
//import FrontendService from '@/components/services/FrontendService'
Vue.use(Vuex)

const MovimentacaoStore = new Vuex.Store({
  state: {
    loading: false,
    movimentos: [],

    tipos: [],
    loadingTipos: false,
  },
  mutations: {
    setLoading(state, value) { state.loading = value },
    setLoadingTipos(state, value) { state.loadingTipos = value },
    
    setMovimentos(state, value) { state.movimentos = value },
    setTipos(state, value) { state.tipos = value },
  },
  getters:{ 
  },
  actions: {
    get_movimentos: async (context)=>{
      const req = new MovimentacaoService()
      context.commit('setLoading', true)
      return await req.listar()
      .then( response => { 
        console.log('movimentos',response.data)
        context.commit('setMovimentos', response.data)
      }).catch( error => { 
        console.error(error.response); 
        context.commit('setMovimentos', [])
      }).finally( () => { 
        context.commit('setLoading', false) 
      })
    },
    get_tipos: async (context)=>{
      const req = new MovimentacaoService()
      context.commit('setLoadingTipos', true)
      return await req.tipos()
      .then( response => { 
        console.log('tipos',response.data)
        context.commit('setTipos', response.data)
      }).catch( error => { 
        console.error(error.response); 
        context.commit('setTipos', [])
      }).finally( () => { 
        context.commit('setLoadingTipos', false) 
      })
    },
    post_movimento: async (context, movimento)=>{
      const req = new MovimentacaoService()
      context.commit('setLoading', true)
      return await req.cadastrar(movimento)
    },
    patch_movimento: async (context, movimento)=>{
      const req = new MovimentacaoService()
      context.commit('setLoading', true)
      return await req.alterar(movimento.id, movimento)
    },
    delete_movimento: async (context, movimento)=>{
      const req = new MovimentacaoService()
      context.commit('setLoading', true)
      return await req.deletar(movimento.id)
      .then( () => {
        alert(`Movimento #${movimento.id} excluído com sucesso`)
        context.dispatch('get_movimentos')
      }).catch( error => { 
        alert(`Falha na exclusão do movimento #${movimento.id}`)
        console.error(error.response);
      }).finally( () => { 
        context.commit('setLoading', false) 
      })
    },
  }
})

export default MovimentacaoStore