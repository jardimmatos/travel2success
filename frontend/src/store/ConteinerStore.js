import Vue from 'vue'
import Vuex from 'vuex'
import ConteinerService from '@/services/ConteinerService'

Vue.use(Vuex)

const ConteinerStore = new Vuex.Store({
  state: {
    loading: false,
    loadingCategorias: false,
    loadingTipos: false,
    loadingStatuses: false,
    conteineres: [],
    categorias: [],
    tipos: [],
    statuses: [],
  },
  mutations: {
    setLoading(state, value) { state.loading = value },
    setLoadingCategorias(state, value) { state.loadingCategorias = value },
    setLoadingTipos(state, value) { state.loadingTipos = value },
    setLoadingStatuses(state, value) { state.loadingStatuses = value },
    
    setConteineres(state, value) { state.conteineres = value },
    setCategorias(state, value) { state.categorias = value },
    setTipos(state, value) { state.tipos = value },
    setStatuses(state, value) { state.statuses = value },
  },
  getters:{ 
  },
  actions: {
    get_conteineres: async (context)=>{
      const req = new ConteinerService()
      context.commit('setLoading', true)
      return await req.listar()
      .then( response => { 
        context.commit('setConteineres', response.data)
      }).catch( error => { 
        console.error(error.response); 
        context.commit('setConteineres', [])
      }).finally( () => { 
        context.commit('setLoading', false) 
      })
    },
    get_categorias: async (context)=>{
      const req = new ConteinerService()
      context.commit('setLoadingCategorias', true)
      return await req.categorias()
      .then( response => { 
        context.commit('setCategorias', response.data)
      }).catch( error => { 
        console.error(error.response); 
        context.commit('setCategorias', [])
      }).finally( () => { 
        context.commit('setLoadingCategorias', false) 
      })
    },
    get_tipos: async (context)=>{
      const req = new ConteinerService()
      context.commit('setLoadingTipos', true)
      return await req.tipos()
      .then( response => { 
        context.commit('setTipos', response.data)
      }).catch( error => { 
        console.error(error.response); 
        context.commit('setTipos', [])
      }).finally( () => { 
        context.commit('setLoadingTipos', false) 
      })
    },
    get_statuses: async (context)=>{
      const req = new ConteinerService()
      context.commit('setLoadingStatuses', true)
      return await req.statuses()
      .then( response => { 
        context.commit('setStatuses', response.data)
      }).catch( error => { 
        console.error(error.response); 
        context.commit('setStatuses', [])
      }).finally( () => { 
        context.commit('setLoadingStatuses', false) 
      })
    },
    post_conteiner: async (context, conteiner)=>{
      const req = new ConteinerService()
      context.commit('setLoading', true)
      return await req.cadastrar(conteiner)
    },
    patch_conteiner: async (context, conteiner)=>{
      const req = new ConteinerService()
      context.commit('setLoading', true)
      return await req.alterar(conteiner.id, conteiner)
    },
    delete_conteiner: async (context, conteiner)=>{
      const req = new ConteinerService()
      context.commit('setLoading', true)
      return await req.deletar(conteiner.id)
      .then( () => {
        alert(`Contêiner ${conteiner.numero} excluído com sucesso`)
        context.dispatch('get_conteineres')
      }).catch( error => { 
        alert(`Falha na exclusão do contêiner #${conteiner.numero}`)
        console.error(error.response);
      }).finally( () => { 
        context.commit('setLoading', false) 
      })
    },
  }
})

export default ConteinerStore
