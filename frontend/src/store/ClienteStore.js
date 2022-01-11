import Vue from 'vue'
import Vuex from 'vuex'
import ClienteService from '@/services/ClienteService'

Vue.use(Vuex);

const ClienteStore = new Vuex.Store({
  state: {
    loading: false,
    clientes: [],
  },
  mutations: {
    setLoading(state, value) { state.loading = value },
    
    setClientes(state, value) { state.clientes = value },
  },
  getters:{ 
  },
  actions: {
    get_clientes: async (context)=>{
      const req = new ClienteService()
      context.commit('setLoading', true)
      return await req.listar()
      .then( response => { 
        context.commit('setClientes', response.data)
      }).catch( error => { 
        console.error(error.response); 
        context.commit('setClientes', [])
      }).finally( () => { 
        context.commit('setLoading', false) 
      })
    },
    post_cliente: async (context, cliente)=>{
      const req = new ClienteService()
      context.commit('setLoading', true)
      return await req.cadastrar(cliente);
      
    },
    patch_cliente: async (context, cliente)=>{
      const req = new ClienteService()
      context.commit('setLoading', true)
      return await req.alterar(cliente.id, cliente)
      
    },
    delete_cliente: async (context, cliente)=>{
      const req = new ClienteService()
      context.commit('setLoading', true)
      return await req.deletar(cliente.id)
      .then( () => {
        alert(`Cliente ${cliente.nome} excluído com sucesso`)
        context.dispatch('get_clientes')
      }).catch( error => { 
        alert(`Falha na exclusão do cliente #${cliente.nome}`)
        console.error(error.response);
      }).finally( () => { 
        context.commit('setLoading', false) 
      })
    },
  }
})

export default ClienteStore
