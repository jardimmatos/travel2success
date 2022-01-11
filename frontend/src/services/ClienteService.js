import BackendService from '@/services/BackendService'

class ClienteService extends BackendService {
    
    constructor(){

        super('clientes', {})
    }

    
    listar(){
        return this.get('/')
    }

    cadastrar(objeto){
        return this.post('/', objeto)
    }
    
    alterar(pk, data){
        return this.patch(`/${pk}/`,data)
    }
    
    deletar(pk){
        return this.delete(`/${pk}/`)
    }
    
}

export default ClienteService