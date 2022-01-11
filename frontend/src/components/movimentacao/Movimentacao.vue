<template>
  <v-dialog scrollable v-model="dialog" :fullscreen="$vuetify.breakpoint.smAndDown" hide-overlay transition="dialog-bottom-transition" width="80%">
    <template v-slot:activator="{ on, attrs }">
      <v-btn color="primary" dark v-bind="attrs" v-on="on" elevation="0" class="mr-1" small>
        Movimentações <v-icon small>mdi-swap-vertical</v-icon>
      </v-btn>
    </template>
    <v-card>
        <v-toolbar dark color="primary">
            <v-btn icon dark @click="dialog = false">
                <v-icon>mdi-close</v-icon>
            </v-btn>
            <v-toolbar-title>Movimentações de contêineres</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-toolbar-items>
                <v-btn dark text @click="dialog = false"> Fechar </v-btn>
            </v-toolbar-items>
        </v-toolbar>
        <v-card-title>
            <MovimentacaoForm :object="modelMovimento"/>
            <v-btn small @click.stop="loadMovimentacoes" :loading="computedIsLoading" color="primary" elevation="0" class="mx-1">
                <v-icon small class="mr-2">mdi-refresh</v-icon> Atualizar
              </v-btn>
            <v-spacer></v-spacer>
            <v-text-field outlined dense v-model="search" append-icon="mdi-magnify" label="Buscar" single-line hide-details></v-text-field>
            
        </v-card-title>
        
        <v-card-text class="pt-4">
          <v-data-table 
              :loading="computedIsLoading"
              :headers="headers" 
              :items="$store.Movimentacao.state.movimentos" 
              :search="search"
              :sort-by="[]"
              :sort-desc="[]"
              elevation="1" 
              no-data-text="Nenhum movimento encontrado"
              no-results-text="Nenhum movimento encontrado"
              loading-text="Carregando..."
              >

              <template v-slot:item.opcoes="{ item }">
                  <v-btn dark color="error" @click="deletar(item)" small elevation="0" outlined title="Excluir" class="mr-1">
                    Excluir
                  </v-btn>
                  <MovimentacaoForm :object="item"/>
              </template>
              <template v-slot:item.get_conteiner.numero="{ item }">
                <strong>
                  <span :title="item.get_conteiner.get_cliente.nome">{{item.get_conteiner.numero}} </span>
                </strong>
              </template>
              <template v-slot:item.inicio="{ item }">
                <span>{{item.inicio|formatarData}}</span>
              </template>
              <template v-slot:item.fim="{ item }">
                <span>{{item.fim|formatarData}}</span>
              </template>
          </v-data-table>
        </v-card-text>
        
    </v-card>
  </v-dialog>
</template>

<script>
import MovimentacaoForm from '@/components/movimentacao/MovimentacaoForm'

  export default {
    name: 'Movimentos',
    components:{
      MovimentacaoForm
    },
    data () {
      return {
        modelMovimento:{
          conteiner: null,
          tipo: null,
          inicio: null,
          fim: null,
        },
        search:'',
        dialog: false,
        headers: [
          { text: 'Conteiner', align: 'start', sortable: true, value: 'get_conteiner.numero', },
          { text: 'Tipo', align: 'start', sortable: true, value: 'tipo', },
          { text: 'início', align: 'center', sortable: true, value: 'inicio', width:'100'},
          { text: 'Término', value: 'fim', sortable: true, width:'100' },
          { text: 'Opções', value: 'opcoes', sortable: false, align:'center' },
        ],
      }
    },
    methods: {
        alterar(obj){
            if(obj)
                this.$store.Movimentacao.dispatch('patch_movimento',obj)
        },
        deletar(movimentacao){
          let excluir = confirm('Confirmar exclusão de movimentação?');
          if (excluir){
            this.$store.Movimentacao.dispatch('delete_movimento', movimentacao)
          }
        },
        loadMovimentacoes(){
            this.$store.Movimentacao.dispatch('get_movimentos')
        },
    },
    computed:{
        computedIsLoading(){
            return this.$store.Movimentacao.state.loading || this.$store.Movimentacao.state.loadingTipos
        },
    },
    mounted(){
        this.loadMovimentacoes()
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