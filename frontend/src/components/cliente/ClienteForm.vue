<template>
  <v-dialog v-model="dialog" fullscreen hide-overlay transition="dialog-bottom-transition">
    <template v-slot:activator="{ on, attrs }">
      <v-btn color="primary" dark v-bind="attrs" v-on="on" elevation="0" class="mr-1" small>
        {{ object.id ? 'Alterar' : 'Cadastrar'}}
      </v-btn>
    </template>
    <v-card>
        <v-toolbar dark color="primary">
            <v-btn icon dark @click="dialog = false">
                <v-icon>mdi-close</v-icon>
            </v-btn>
            <v-toolbar-title>
                {{object.id ? 'Alteração de ' :'Cadastro de '}} Cliente
            </v-toolbar-title>
            <v-spacer></v-spacer>
            <v-toolbar-items>
                <v-btn dark text @click="dialog = false"> Fechar </v-btn>
            </v-toolbar-items>
        </v-toolbar>
        <v-card-text>
            <div class="pt-2">
                <v-row dense class="pa-2">
                    Cliente: <span class="subtitle-2 font-weight-black"> {{cliente.nome}}</span>
                </v-row>
                <v-row dense>               
                    <!-- NOME -->
                    <v-col cols="12" sm="12">
                        <v-text-field outlined dense required v-model="cliente.nome" autofocus
                            label="Nome" 
                            v-validate="{ required: true }"
                            data-vv-as="Nome"
                            :messages="veeErrors.first('input-nome')"
                            data-vv-name="input-nome"
                            :class="veeErrors.has('input-nome') ? 'v-input--has-state error--text' : ''"
                            clearable>
                            <template v-slot:message="{message}">
                                <span class="error--text">{{message}}</span>
                            </template>
                        </v-text-field>
                    </v-col>

                    <!-- DOCUMENTO -->
                    <v-col cols="12" sm="6">
                        <v-text-field outlined dense required v-model="cliente.documento"
                            label="CPF" 
                            v-mask="'###.###.###-##'"
                            v-validate="{ required: true }"
                            data-vv-as="CPF"
                            :messages="veeErrors.first('input-documento')"
                            data-vv-name="input-documento"
                            :class="veeErrors.has('input-documento') ? 'v-input--has-state error--text' : ''"
                            clearable>
                            <template v-slot:message="{message}">
                                <span class="error--text">{{message}}</span>
                            </template>
                        </v-text-field>
                    </v-col>

                    <!-- CEP -->
                    <v-col cols="12" sm="6">
                        <v-text-field outlined dense clearable
                            label="CEP" 
                            v-model="cliente.cep"
                            :loading="loading"
                            @blur="onCEP($event.target.value)"
                            v-mask="'#####-###'"
                            :messages="loading ? 'Pesquisando CEP...':''"
                            >
                            <template v-slot:message="{message}">
                                <span class="secondary--text">{{message}}</span>
                            </template>
                        </v-text-field>
                    </v-col>
                    
                    <!-- ENDERECO -->
                    <v-col cols="12" sm="12">
                        <v-text-field outlined dense required v-model="cliente.endereco" clearable
                            label="Endereço" >
                        </v-text-field>
                    </v-col>

                    <!-- Bairro -->
                    <v-col cols="12" sm="6">
                        <v-text-field outlined dense required v-model="cliente.bairro" clearable
                            label="Bairro">
                        </v-text-field>
                    </v-col>

                    <!-- Cidade -->
                    <v-col cols="12" sm="6">
                        <v-text-field outlined dense required v-model="cliente.cidade" clearable
                            label="Cidade">
                        </v-text-field>
                    </v-col>

                    <!-- UF's -->
                    <v-col cols="12" sm="6" md="6">
                        <v-autocomplete clearable hide-selected outlined dense 
                            no-data-text="Nenhum registro"
                            v-model="cliente.uf"
                            :items="ufs" 
                            item-value="uf"
                            item-text="unidade"
                            label="UF" placeholder="Informe o Estado">
                        </v-autocomplete>
                    </v-col>

                </v-row>
            </div>
        </v-card-text>
        <v-card-actions>
            <v-btn @click.stop="onSubmit" :loading="$store.Cliente.state.loading" elevation="0" color="primary">
                <v-icon small class="mr-2">mdi-checkbox-marked-circle-outline</v-icon> Salvar 
            </v-btn>
        </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import axios from 'axios'
import FrontendService from '@/services/FrontendService'

export default {
    props:{
        object:{
            required:true
        }
    },
	name: 'ClienteForm',
	components: {
	},
	data(){
		return {
            loading: false,
            dialog:false,
			cliente:{},
            ufs:[
                { uf:'AC', unidade:'Acre' },
                { uf:'AL', unidade:'Alagoas' },
                { uf:'AM', unidade:'Amazonas' },
                { uf:'AP', unidade:'Amapá' },
                { uf:'BA', unidade:'Bahia' },
                { uf:'CE', unidade:'Ceará' },
                { uf:'DF', unidade:'Distrito Federal' },
                { uf:'ES', unidade:'Espírito Santo' },
                { uf:'GO', unidade:'Goiás' },
                { uf:'MA', unidade:'Maranhão' },
                { uf:'MG', unidade:'Minas Gerais' },
                { uf:'MS', unidade:'Mato Grosso do Sul' },
                { uf:'MT', unidade:'Mato Grosso' },
                { uf:'PA', unidade:'Pará' },
                { uf:'PB', unidade:'Paraíba' },
                { uf:'PI', unidade:'Piauí' },
                { uf:'PE', unidade:'Pernambuco' },
                { uf:'PR', unidade:'Paraná' },
                { uf:'RJ', unidade:'Rio de Janeiro' },
                { uf:'RN', unidade:'Rio Grande do Norte' },
                { uf:'RO', unidade:'Rondônia' },
                { uf:'RR', unidade:'Roraima' },
                { uf:'RS', unidade:'Rio Grande do Sul' },
                { uf:'SC', unidade:'Santa Catarina' },
                { uf:'SE', unidade:'Sergipe' },
                { uf:'SP', unidade:'São Paulo' },
                { uf:'TO', unidade:'Tocantins' },
            ]
		}
	},
	methods:{
        onCEP(value){
            let cep = value
            if(cep.length == 9){
                this.loading = true
                axios.get(`https://viacep.com.br/ws/${cep.replace("-","")}/json`)
                    .then(response => {
                        this.cliente.endereco = response.data.logradouro
                        this.cliente.bairro = response.data.bairro
                        this.cliente.cidade = response.data.localidade
                        this.cliente.uf = response.data.uf
                    })
                    .catch( () => {
                        //
                    }).finally(()=>{
                        this.loading = false
                    })
            }
        },
        limparErrors(){
            this.veeErrors.clear()
        },
        veeValidateField(ref) {
            if ( this.veeFields[ref] && (this.veeFields[ref].dirty || this.veeFields[ref].validated)) {
                return !this.veeErrors.has(ref);
            }
            return null;
        },
        cadastrar(){
            const request = this.$store.Cliente.dispatch('post_cliente', this.cliente)
            this.$store.Cliente.commit('setLoading', true)
            request.then( () => { 
                    alert(`Cliente ${this.cliente.nome} cadastrado com sucesso`)
                    this.initObject()
                    this.$store.Cliente.dispatch('get_clientes')
                    this.dialog = false
                }).catch( error => { 
                    console.error(error.response); 
                    let msg = FrontendService.tryResonseErrorStringToJson(error.response.data)
                    alert(`Falha no cadastro do cliente\n\n${msg}`)
                }).finally( () => { 
                    this.$store.Cliente.commit('setLoading', false) 
                    this.limparErrors()
                })
        },
        alterar(){
            const request = this.$store.Cliente.dispatch('patch_cliente', this.cliente)
            this.$store.Cliente.commit('setLoading', true)
            request.then( () => {
                alert(`Cliente ${this.cliente.nome} alterado com sucesso`)
                this.$store.Cliente.dispatch('get_clientes')
                this.dialog = false
            }).catch( error => { 
                console.error(error.response);
                let msg = FrontendService.tryResonseErrorStringToJson(error.response.data)
                alert(`Falha na alteração do cliente\n\n${msg}`)
            }).finally( () => { 
                this.$store.Cliente.commit('setLoading', false)
            })
        },
        onSubmit(){
            this.$validator.validateAll()
                .then(success => {
                    if (!success) {
                        return;
                    }
                    
                    if(this.object.id){
                        this.alterar()
                    }else{
                        this.cadastrar()
                    }
                })
                .catch( error => {
                    console.error('onSubmit', error)  
                });
        },
        initObject(){
            this.cliente = Object.assign({}, this.object)
            this.limparErrors()
        }
        
    },
    computed:{
    },
    created(){
    },
    mounted(){
    },
    watch:{
        dialog(value){
            if (value){
                this.initObject()
            }
        }
    }
}
</script>