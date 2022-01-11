const dictionary = {
    pt: {
        messages: {
            required: (field) => `${field} é obrigatório.`,
            regex: (field) => `${field} não corresponde à expressão correta.`,
            min: (field,size) => {
                return `${size} caracteres são necessários`
            },
            max: (field,size) => {
                return `Máximo de ${size} caracteres, atingido!`
            },
            between: (field, params) => `${field} deve estar entre ${params[0]} e ${params[1]}`,
            included: () => `Necessário selecionar uma opção` 
        }
    }
}
export default dictionary