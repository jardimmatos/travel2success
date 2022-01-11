<template>
  <v-dialog scrollable v-model="dialog" :fullscreen="$vuetify.breakpoint.mdAndDown" hide-overlay transition="dialog-bottom-transition" width="60%">
    <template v-slot:activator="{ on, attrs }">
      <v-btn color="primary" dark v-bind="attrs" v-on="on" elevation="0" class="mr-1" small>
        Clientes <v-icon small>mdi-account-multiple</v-icon>
      </v-btn>
    </template>
    <v-card>
        <v-toolbar dark color="primary">
            <v-btn icon dark @click="dialog = false">
                <v-icon>mdi-close</v-icon>
            </v-btn>
            <v-toolbar-title>Gestão de clientes</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-toolbar-items>
                <v-btn dark text @click="dialog = false"> Fechar </v-btn>
            </v-toolbar-items>
        </v-toolbar>
        <v-card-title>
          <ClienteForm :object="modelCliente"/>
          <v-btn small @click.stop="loadClientes" :loading="computedIsLoading" color="primary" elevation="0" class="mx-1">
            <v-icon small class="mr-2">mdi-refresh</v-icon> Atualizar
          </v-btn>
          <v-spacer></v-spacer>
          <v-text-field outlined dense v-model="search" append-icon="mdi-magnify" label="Buscar" single-line hide-details></v-text-field>
        </v-card-title>
        <v-card-text class="pt-4">

          <v-data-table 
              :headers="headers" 
              :items="$store.Cliente.state.clientes" 
              :search="search"
              :sort-by="['nome']"
              :sort-desc="[false]"
              elevation="1" 
              no-data-text="Nenhum cliente encontrado"
              no-results-text="Nenhum cliente encontrado"
              loading-text="Carregando..."
              >
              
              <template v-slot:item.endereco_completo="{ item }">
                  <div>{{ item.cep }}</div> 
                  <div>{{ item.endereco }} {{ item.bairro }}</div>
                  <div>{{ item.cidade }} - {{ item.uf }}</div>
              </template>

              <template v-slot:item.opcoes="{ item }">
                  <v-btn dark color="error" @click="deletar(item)" small elevation="0" outlined title="Excluir" class="mr-1">
                    Excluir
                  </v-btn>
                  <ClienteForm :object="item"/>
              </template>
              
          </v-data-table>
        </v-card-text>
        
    </v-card>
  </v-dialog>
</template>

<script>
import ClienteForm from '@/components/cliente/ClienteForm'

  export default {
    name: 'Cliente',
    components:{
      ClienteForm
    },
    data () {
      return {
        modelCliente:{
          nome:null,
          documento:null,
          cep:null,
          endereco:null,
          bairro:null,
          cidade:null,
          uf:null,
        },
        required: [v => (v||'').length > 0 || 'Campo obrigatório'],
        search:'',
        dialog: false,
        headers: [
          //{ text: 'ID', align: 'center', sortable: true, value: 'id', },
          { text: 'Nome', align: 'start', sortable: true, value: 'nome', },
          { text: 'documento', align: 'start', sortable: true, value: 'documento', width:'150' },
          { text: 'Endereco', value: 'endereco_completo', sortable: false },
          { text: 'Opções', value: 'opcoes', sortable: false, width:"210" },
        ],
      }
    },
    methods: {
        alterar(obj){
            if(obj)
                this.$store.Cliente.dispatch('patch_cliente',obj)
        },
        deletar(cliente){
          let excluir = confirm('Confirmar exclusão de cliente?');
          if (excluir){
            this.$store.Cliente.dispatch('delete_cliente', cliente)
          }
        },
        loadClientes(){
            this.$store.Cliente.dispatch('get_clientes')
        },
    },
    computed:{
        computedIsLoading(){
            return this.$store.Cliente.state.loading
        },
    },
    mounted(){
        this.loadClientes()
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