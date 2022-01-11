class FrontendService {

    static tryResonseErrorStringToJson(response){
        let mensagens = []
        try{
            try{
                let errors = response.map(obj =>{
                    // Antes de realizar o parse para JSON alterar a string de aspas simples para aspas duplas
                    return obj.replaceAll("'",'"')
                })
                //alterar de string para JSON
                errors = JSON.parse(errors)
                let keys = Object.keys(errors)
                mensagens = keys.map(obj =>{
                    //Recuperar sempre a primeira mensagem de erro  dos objetos capturados pelas chaves
                    return errors[obj][0]
                })
            }catch{
                // quando array de strings
                let keys = Object.keys(response)
                return response[keys[0]]
            }
        }catch{
            console.error('errors',response)
        }
        return mensagens
    }    
}

export default FrontendService