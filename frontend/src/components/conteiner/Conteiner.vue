<template>
  <v-dialog scrollable v-model="dialog" :fullscreen="$vuetify.breakpoint.mdAndDown" hide-overlay transition="dialog-bottom-transition" width="60%">
    <template v-slot:activator="{ on, attrs }">
      <v-btn color="primary" dark v-bind="attrs" v-on="on" elevation="0" class="mr-1" small>
        Conteiners <v-icon small>mdi-checkerboard</v-icon>
      </v-btn>
    </template>
    <v-card>
        <v-toolbar dark color="primary">
            <v-btn icon dark @click="dialog = false">
                <v-icon>mdi-close</v-icon>
            </v-btn>
            <v-toolbar-title>Gestão de contêiners</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-toolbar-items>
                <v-btn dark text @click="dialog = false"> Fechar </v-btn>
            </v-toolbar-items>
        </v-toolbar>
        <v-card-title>
            <ContainerForm :object="modelConteiner"/>
            <v-btn small @click.stop="loadConteineres" :loading="computedIsLoading" color="primary" elevation="0" class="mx-1">
                <v-icon small class="mr-2">mdi-refresh</v-icon> Atualizar
              </v-btn>
            <v-spacer></v-spacer>
            <v-text-field outlined dense v-model="search" append-icon="mdi-magnify" label="Buscar" single-line hide-details></v-text-field>
            
        </v-card-title>
        <v-card-text class="pt-4">

          <v-data-table 
              :loading="computedIsLoading"
              :headers="headers" 
              :items="$store.Conteiner.state.conteineres" 
              :search="search"
              :sort-by="['nome']"
              :sort-desc="[false]"
              elevation="1" 
              no-data-text="Nenhum cliente encontrado"
              no-results-text="Nenhum cliente encontrado"
              loading-text="Carregando..."
              >

              <template v-slot:item.numero="{ item }">
                <strong>{{item.numero}}</strong>
              </template>
              <template v-slot:item.opcoes="{ item }">
                  <v-btn dark color="error" @click="deletar(item)" small elevation="0" outlined title="Excluir" class="mr-1">
                    Excluir
                  </v-btn>
                  <ContainerForm :object="item"/>
              </template>
          </v-data-table>
        </v-card-text>
        
    </v-card>
  </v-dialog>
</template>

<script>
import ContainerForm from '@/components/conteiner/ConteinerForm'

  export default {
    name: 'Conteiner',
    components:{
      ContainerForm
    },
    data () {
      return {
        modelConteiner:{
          cliente: null,
          categoria: null,
          tipo: null,
          status: null,
          numero: null
        },
        required: [v => (v||'').length > 0 || 'Campo obrigatório'],
        search:'',
        dialog: false,
        headers: [
          { text: 'Número', align: 'center', sortable: true, value: 'numero', },
          { text: 'Cliente', align: 'start', sortable: true, value: 'get_cliente.nome', },
          { text: 'Categoria', align: 'start', sortable: true, value: 'categoria', width:"50"},
          { text: 'Status', value: 'status', sortable: true, width:"50" },
          { text: 'Tipo', value: 'tipo', sortable: true, width:"50" },
          { text: 'Opções', value: 'opcoes', sortable: false, align: 'center' },
        ],
      }
    },
    methods: {
        alterar(obj){
            if(obj)
                this.$store.Conteiner.dispatch('patch_conteiner',obj)
        },
        deletar(conteiner){
          let excluir = confirm('Confirmar exclusão de contêiner?');
          if (excluir){
            this.$store.Conteiner.dispatch('delete_conteiner', conteiner)
          }
        },
        loadConteineres(){
            this.$store.Conteiner.dispatch('get_conteineres')
        },
    },
    computed:{
        computedIsLoading(){
            return this.$store.Conteiner.state.loading
        },
    },
    mounted(){
        this.loadConteineres()
    },
    watch:{
    }
}
    
</script>

<style scoped>
.v-small-dialog__content .v-input:last-child{
    padding-bottom: 10px !important;
}
</style>