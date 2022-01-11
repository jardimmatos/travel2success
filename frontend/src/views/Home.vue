<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <v-img src="https://www.seekpng.com/png/full/849-8494457_century-21-logo-vector-free-download-aperto-de.png"
          class="my-12" contain height="200"/>
      </v-col>

      <v-col class="my-1" cols="12">
        <Cliente/>
        <Conteiner/>
        <Movimentacao/>
        <Relatorio/>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Cliente from '@/components/cliente/Cliente'
import Conteiner from '@/components/conteiner/Conteiner'
import Movimentacao from '@/components/movimentacao/Movimentacao'
import Relatorio from '@/components/relatorio/Relatorio'

  export default {
    name: 'Home',
    components:{
      Cliente, 
      Conteiner, 
      Movimentacao, 
      Relatorio
    },
  }
</script>
