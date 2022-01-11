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
                {{object.id ? 'Alteração de ' :'Cadastro de '}} Contêiner
            </v-toolbar-title>
            <v-spacer></v-spacer>
            <v-toolbar-items>
                <v-btn dark text @click="dialog = false"> Fechar </v-btn>
            </v-toolbar-items>
        </v-toolbar>
        <v-card-text>
            <div class="pt-2">
                <v-row dense class="pa-2">
                    Contêiner: <span class="subtitle-2 font-weight-black"> {{conteiner.numero}}</span>
                </v-row>
                <v-row dense>               
                    <!-- NUMERO -->
                    <v-col cols="12" sm="12">
                        <v-text-field outlined dense required v-model="conteiner.numero" autofocus
                            maxlength="11"
                            label="Número"  placeholder="ABCD1234567 (padrão para o número)"
                            v-validate="{ required: true, regex:/^[a-zA-Z]{4}[0-9]{7}$/ }"
                            data-vv-as="Número"
                            :messages="veeErrors.first('input-numero')"
                            data-vv-name="input-numero"
                            :class="veeErrors.has('input-numero') ? 'v-input--has-state error--text' : ''"
                            clearable>
                            <template v-slot:message="{message}">
                                <span class="error--text">{{message}}</span>
                            </template>
                        </v-text-field>
                    </v-col>

                    <!-- CLIENTE -->
                    <v-col cols="12" sm="6" md="6">
                        <v-autocomplete clearable hide-selected outlined dense 
                            no-data-text="Nenhum registro"
                            v-model="conteiner.cliente"
                            :loading="$store.Cliente.state.loading"
                            :items="$store.Cliente.state.clientes" 
                            item-value="id"
                            item-text="nome"
                            label="Cliente" placeholder="Informe um cliente"
                            v-validate="{ required: true }"
                            data-vv-as="Cliente"
                            :messages="veeErrors.first('input-cliente')"
                            data-vv-name="input-cliente"
                            :class="veeErrors.has('input-cliente') ? 'v-input--has-state error--text' : ''"
                            >
                            <template v-slot:message="{message}">
                                <span class="error--text">{{message}}</span>
                            </template>
                        </v-autocomplete>
                    </v-col>

                    <!-- CATEGORIA -->
                    <v-col cols="12" sm="6" md="6">
                        <v-autocomplete clearable hide-selected outlined dense 
                            no-data-text="Nenhum registro"
                            v-model="conteiner.categoria"
                            :loading="$store.Conteiner.state.loadingCategorias"
                            :items="$store.Conteiner.state.categorias" 
                            item-value="name"
                            item-text="value"
                            label="Categoria" placeholder="Informe uma categoria"
                            v-validate="{ required: true }"
                            data-vv-as="Categoria"
                            :messages="veeErrors.first('input-categoria')"
                            data-vv-name="input-categoria"
                            :class="veeErrors.has('input-categoria') ? 'v-input--has-state error--text' : ''"
                            >
                            <template v-slot:message="{message}">
                                <span class="error--text">{{message}}</span>
                            </template>
                        </v-autocomplete>
                    </v-col>

                    <!-- TIPOS -->
                    <v-col cols="12" sm="6" md="6">
                        <v-autocomplete clearable hide-selected outlined dense 
                            no-data-text="Nenhum registro"
                            v-model="conteiner.tipo"
                            :items="$store.Conteiner.state.tipos" 
                            :loading="$store.Conteiner.state.loadingTipos"
                            item-value="value"
                            item-text="value"
                            label="Tipos" placeholder="Informe um tipo"
                            v-validate="{ required: true }"
                            data-vv-as="Tipo"
                            :messages="veeErrors.first('input-tipo')"
                            data-vv-name="input-tipo"
                            :class="veeErrors.has('input-tipo') ? 'v-input--has-state error--text' : ''"
                            >
                            <template v-slot:message="{message}">
                                <span class="error--text">{{message}}</span>
                            </template>
                        </v-autocomplete>
                    </v-col>

                    <!-- STATUSES -->
                    <v-col cols="12" sm="6" md="6">
                        <v-autocomplete clearable hide-selected outlined dense 
                            no-data-text="Nenhum registro"
                            v-model="conteiner.status"
                            :items="$store.Conteiner.state.statuses" 
                            :loading="$store.Conteiner.state.loadingStatuses"
                            item-value="name"
                            item-text="value"
                            label="Status" placeholder="Informe um status"
                            v-validate="{ required: true }"
                            data-vv-as="Status"
                            :messages="veeErrors.first('input-status')"
                            data-vv-name="input-status"
                            :class="veeErrors.has('input-status') ? 'v-input--has-state error--text' : ''"
                            >
                            <template v-slot:message="{message}">
                                <span class="error--text">{{message}}</span>
                            </template>
                        </v-autocomplete>
                    </v-col>

                </v-row>

            </div>
        </v-card-text>
        <v-card-actions>
            <v-btn v-if="computedObjetoAlterado" @click.stop="onSubmit" 
                :loading="$store.Conteiner.state.loading" elevation="0" color="primary">
                <v-icon small class="mr-2">mdi-checkbox-marked-circle-outline</v-icon> Salvar 
            </v-btn>
        </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
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
			conteiner:{},
		}
	},
	methods:{
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
            this.$store.Conteiner.commit('setLoading', true)
            const request = this.$store.Conteiner.dispatch('post_conteiner', this.conteiner)
            request.then( () => { 
                    alert(`Contêiner ${this.conteiner.numero} cadastrado com sucesso`)
                    this.$store.Conteiner.dispatch('get_conteineres')
                    this.dialog=false
                }).catch( error => { 
                    console.error(error.response); 
                    let msg = FrontendService.tryResonseErrorStringToJson(error.response.data)
                    alert(`Falha no cadastro do contêiner\n\n${msg}`)
                }).finally( () => { 
                    this.$store.Conteiner.commit('setLoading', false) 
                })
        },
        alterar(){
            const request = this.$store.Conteiner.dispatch('patch_conteiner', this.conteiner)
            this.$store.Conteiner.commit('setLoading', true)
            request.then( () => { 
                    alert(`Contêiner ${this.conteiner.numero} alterado com sucesso`)
                    this.$store.Conteiner.dispatch('get_conteineres')
                    this.dialog=false
                }).catch( error => { 
                    console.error(error.response); 
                    let msg = FrontendService.tryResonseErrorStringToJson(error.response.data)
                    alert(`Falha na alteração do contêiner\n\n${msg}`)
                }).finally( () => { 
                    this.$store.Conteiner.commit('setLoading', false) 
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
            this.conteiner = Object.assign({}, this.object)
            this.limparErrors()
        },
        loadResources(){
            this.$store.Conteiner.dispatch('get_categorias')
            this.$store.Conteiner.dispatch('get_tipos')
            this.$store.Conteiner.dispatch('get_statuses')
            this.$store.Cliente.dispatch('get_clientes')
        }
    },
    computed:{
        computedObjetoAlterado(){
            return JSON.stringify(this.object) !== JSON.stringify(this.conteiner)
        }
    },
    created(){
    },
    mounted(){
        this.loadResources()
    },
    watch:{
        dialog(value){
            if(value){
                this.initObject()
            }
        }
    }
}
</script>