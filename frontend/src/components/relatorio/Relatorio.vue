<template>
  <v-dialog scrollable v-model="dialog" :fullscreen="$vuetify.breakpoint.mdAndDown" hide-overlay transition="dialog-bottom-transition" width="60%">
    <template v-slot:activator="{ on, attrs }">
      <v-btn color="primary" dark v-bind="attrs" v-on="on" elevation="0" class="mr-1" small>
        Relatório <v-icon small>mdi-chart-bar</v-icon>
      </v-btn>
    </template>
    <v-card>
        <v-toolbar dark color="primary">
            <v-btn icon dark @click="dialog = false">
                <v-icon>mdi-close</v-icon>
            </v-btn>
            <v-toolbar-title>Relatório por cliente e tipo movimentação</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-toolbar-items>
                <v-btn dark text @click="dialog = false"> Fechar </v-btn>
            </v-toolbar-items>
        </v-toolbar>
        <v-card-title>
            <strong>Total de {{computedTotalRegistros}} registros</strong>
            <v-spacer></v-spacer>
            <v-text-field outlined dense v-model="search" append-icon="mdi-magnify" label="Buscar" single-line hide-details></v-text-field>
        </v-card-title>
        
        <v-card-text class="pt-4">

          <v-data-table 
              :loading="computedIsLoading"
              :headers="headers" 
              :items="$store.Relatorio.state.relatorios" 
              :search="search"
              :sort-by="[]"
              :sort-desc="[]"
              elevation="1" 
              no-data-text="Nenhum regisitro encontrado"
              no-results-text="Nenhum registro encontrado"
              loading-text="Carregando..."
              >
              <template v-slot:item.conteiner__cliente__nome="{ item }">
                <strong>{{item.conteiner__cliente__nome}}</strong>
              </template>
              <template v-slot:item.tipo="{ item }">
                <strong>{{item.tipo}}</strong>
              </template>
              <template v-slot:item.total="{ item }">
                <strong>{{item.total}}</strong>
              </template>
          </v-data-table>
        </v-card-text>
        
    </v-card>
  </v-dialog>
</template>

<script>

  export default {
    name: 'Relatorio',
    components:{
    },
    data () {
      return {
        search:'',
        dialog: false,
        headers: [
          { text: 'Cliente', align: 'start', sortable: false, value: 'conteiner__cliente__nome', width:'200' },
          { text: 'Tipo Movimento', align: 'start', sortable: false, value: 'tipo', width:'100'},
          { text: 'Total', align: 'start', sortable: false, value: 'total', width:'100'},
        ],
      }
    },
    methods: {
        loadRelatorios(){
            this.$store.Relatorio.dispatch('get_relatorios')
        },
    },
    computed:{
        computedIsLoading(){
            return this.$store.Relatorio.state.loading
        },
        computedTotalRegistros(){
          let total = this.$store.Relatorio.state.relatorios.reduce((acumulador, obj) => {
              return acumulador += obj.total;
          }, 0)
          return total
        }
    },
    mounted(){
        this.loadRelatorios()
        setInterval(
          ()=> this.loadRelatorios(), 5000
        )
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