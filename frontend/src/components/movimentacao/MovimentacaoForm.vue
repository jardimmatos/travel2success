<template>
  <v-dialog v-model="dialog" fullscreen hide-overlay transition="dialog-bottom-transition">
    <template v-slot:activator="{ on, attrs }">
      <v-btn color="primary" dark v-bind="attrs" v-on="on" elevation="0" class="mr-1" small>
        {{ object.id ? 'Alterar' : 'Registrar'}}
      </v-btn>
    </template>
    <v-card>
        <v-toolbar dark color="primary">
            <v-btn icon dark @click="dialog = false">
                <v-icon>mdi-close</v-icon>
            </v-btn>
            <v-toolbar-title>
                {{object.id ? 'Alteração de ' :'Cadastro de '}} Movimentação
            </v-toolbar-title>
            <v-spacer></v-spacer>
            <v-toolbar-items>
                <v-btn dark text @click="dialog = false"> Fechar </v-btn>
            </v-toolbar-items>
        </v-toolbar>
        <v-card-text>
            <div class="pt-2">
                <v-row dense class="pa-2">
                    Movimentação: <span class="subtitle-2 font-weight-black"> #{{movimento.id}}</span>
                </v-row>
                <v-row dense>

                    <!-- CONTEINER -->
                    <v-col cols="12" sm="6" md="6">
                        <v-autocomplete clearable hide-selected outlined dense 
                            no-data-text="Nenhum registro"
                            v-model="movimento.conteiner"
                            :loading="$store.Conteiner.state.loading"
                            :items="$store.Conteiner.state.conteineres" 
                            item-value="id"
                            item-text="numero"
                            label="Contêiner" placeholder="Informe um contêiner"
                            v-validate="{ required: true }"
                            data-vv-as="Contêiner"
                            :messages="veeErrors.first('input-conteiner')"
                            data-vv-name="input-conteiner"
                            :class="veeErrors.has('input-conteiner') ? 'v-input--has-state error--text' : ''"
                            >
                            <template v-slot:message="{message}">
                                <span class="error--text">{{message}}</span>
                            </template>
                        </v-autocomplete>
                    </v-col>

                    <!-- TIPO -->
                    <v-col cols="12" sm="6" md="6">
                        <v-autocomplete clearable hide-selected outlined dense 
                            no-data-text="Nenhum registro"
                            v-model="movimento.tipo"
                            :items="$store.Movimentacao.state.tipos" 
                            :loading="$store.Movimentacao.state.loadingTipos"
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
                    
                    <!-- INÍCIO DATA-->
                    <v-col cols="12" sm="3">
                        <v-text-field outlined dense required v-model="computed_inicio_data"
                            label="Data Início" type="date"
                            v-validate="{ required: true }"
                            data-vv-as="Data Início"
                            :messages="veeErrors.first('input-inicio-data')"
                            data-vv-name="input-inicio-data"
                            :class="veeErrors.has('input-inicio-data') ? 'v-input--has-state error--text' : ''"
                            >
                            <template v-slot:message="{message}">
                                <span class="error--text">{{message}}</span>
                            </template>
                        </v-text-field>
                    </v-col>

                    <!-- INÍCIO HORA -->
                    <v-col cols="12" sm="3">
                        <v-text-field outlined dense required v-model="computed_inicio_hora"
                            label="Hora Início" type="time"
                            v-validate="{ required: true }"
                            data-vv-as="Hora Início"
                            :messages="veeErrors.first('input-inicio-hora')"
                            data-vv-name="input-inicio-hora"
                            :class="veeErrors.has('input-inicio-hora') ? 'v-input--has-state error--text' : ''"
                            >
                            <template v-slot:message="{message}">
                                <span class="error--text">{{message}}</span>
                            </template>
                        </v-text-field>
                    </v-col>
                    
                    <!-- TERMINO DATA-->
                    <v-col cols="12" sm="3">
                        <v-text-field outlined dense required v-model="computed_fim_data"
                            label="Data Término" type="date"
                            v-validate="{ required: true }"
                            data-vv-as="Data Término"
                            :messages="veeErrors.first('input-fim-data')"
                            data-vv-name="input-fim-data"
                            :class="veeErrors.has('input-fim-data') ? 'v-input--has-state error--text' : ''"
                            >
                            <template v-slot:message="{message}">
                                <span class="error--text">{{message}}</span>
                            </template>
                        </v-text-field>
                    </v-col>

                    <!-- TERMINO HORA -->
                    <v-col cols="12" sm="3">
                        <v-text-field outlined dense required v-model="computed_fim_hora"
                            label="Hora Término" type="time"
                            v-validate="{ required: true }"
                            data-vv-as="Hora Término"
                            :messages="veeErrors.first('input-fim-hora')"
                            data-vv-name="input-fim-hora"
                            :class="veeErrors.has('input-fim-hora') ? 'v-input--has-state error--text' : ''"
                            >
                            <template v-slot:message="{message}">
                                <span class="error--text">{{message}}</span>
                            </template>
                        </v-text-field>
                    </v-col>

                    
                </v-row>

            </div>
        </v-card-text>
        <v-card-actions>
            <v-btn v-if="computedObjetoAlterado" @click.stop="onSubmit" 
                :loading="$store.Movimentacao.state.loading" elevation="0" color="primary">
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
	name: 'MovimentacaoForm',
	components: {
	},
	data(){
		return {
            loading: false,
            dialog:false,
			movimento:{},
            inicio_data:new Date(),
            inicio_hora:'00:00',
            fim_data:null,
            fim_hora:'00:00',
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
            const request = this.$store.Movimentacao.dispatch('post_movimento', this.movimento)
            this.$store.Movimentacao.commit('setLoading', true)
            request.then( () => { 
                alert(`Movimentação registrada com sucesso`)
                this.$store.Movimentacao.dispatch('get_movimentos')
                this.dialog=false
                this.limparErrors()
            }).catch( error => { 
                console.error(error.response); 
                let msg = FrontendService.tryResonseErrorStringToJson(error.response.data)
                alert(`Falha ao registrar movimentação\n\n${msg}`)
            }).finally( () => { 
                this.$store.Movimentacao.commit('setLoading', false) 
            })
        },
        alterar(){
            const request = this.$store.Movimentacao.dispatch('patch_movimento', this.movimento)
            this.$store.Movimentacao.commit('setLoading', true)
            request.then( () => { 
                alert(`Movimentação alterada com sucesso`)
                this.$store.Movimentacao.dispatch('get_movimentos')
                this.dialog=false
            }).catch( error => { 
                console.error(error.response); 
                let msg = FrontendService.tryResonseErrorStringToJson(error.response.data)
                alert(`Falha na alteração do movimento\n\n${msg}`)
            }).finally( () => { 
                this.$store.Movimentacao.commit('setLoading', false) 
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
            this.movimento = Object.assign({}, this.object)
            this.limparErrors()
        },
        loadResources(){
            this.$store.Conteiner.dispatch('get_conteineres')
            this.$store.Movimentacao.dispatch('get_tipos')
        }
    },
    computed:{
        computedObjetoAlterado(){
            return JSON.stringify(this.object) !== JSON.stringify(this.movimento)
        },
        computed_inicio_data:{
            get: function() {
                return (this.movimento.inicio||'').split('T')[0]
            },
            set: function(newValue) {
                let data_original = (this.movimento.inicio||'').split('T')
                this.movimento.inicio = `${newValue}T${data_original[1]}`
            }
        },
        computed_inicio_hora:{
            get: function() {
                return (this.movimento.inicio||'').split('T')[1]
            },
            set: function(newValue) {
                let data_original = (this.movimento.inicio||'').split('T')
                this.movimento.inicio = `${data_original[0]}T${newValue}`
            }
        },
        computed_fim_data:{
            get: function() {
                return (this.movimento.fim||'').split('T')[0]
            },
            set: function(newValue) {
                let data_original = (this.movimento.fim||'').split('T')
                this.movimento.fim = `${newValue}T${data_original[1]}`
            }
        },
        computed_fim_hora:{
            get: function() {
                return (this.movimento.fim||'').split('T')[1]
            },
            set: function(newValue) {
                let data_original = (this.movimento.fim||'').split('T')
                this.movimento.fim = `${data_original[0]}T${newValue}`
            }
        },
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
        },
    }
}
</script>