import BackendService from '@/services/BackendService'

class RelatorioService extends BackendService {
    
    constructor(){

        super('relatorios', {})
    }

    listar(){
        return this.get('/')
    }

}

export default RelatorioService