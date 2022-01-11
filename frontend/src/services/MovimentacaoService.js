import BackendService from '@/services/BackendService'

class MovimentacaoService extends BackendService {
    
    constructor(){

        super('movimentacoes', {})
    }

    
    tipos(){
        return this.get('/tipos/')
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

export default MovimentacaoService