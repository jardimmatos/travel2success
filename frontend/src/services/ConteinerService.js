import BackendService from '@/services/BackendService'

class ConteinerService extends BackendService {
    
    constructor(){

        super('conteineres', {})
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
    
    categorias(){
        return this.get(`/categorias/`)
    }

    tipos(){
        return this.get(`/tipos/`)
    }

    statuses(){
        return this.get(`/statuses/`)
    }
    
}

export default ConteinerService