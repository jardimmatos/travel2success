<template>
  <v-app>
    <v-app-bar app color="primary" dark >
      <div class="d-flex align-center">
        <v-img alt="Icon" class="shrink mr-2" contain  width="30" transition="scale-transition"
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png" style="transform: rotate(270deg);"/>
        DEV
      </div>

      <v-spacer></v-spacer>
    </v-app-bar>

    <v-main>
      <router-view/>
    </v-main>
    <v-footer absolute color="primary" dark>
      <v-col class="text-center" cols="12">
        Desenvolvido por <strong>Agostinho Jardim Matos Júnior</strong>
        - {{ new Date().getFullYear() }} — <strong>Vuetify</strong>
      </v-col>
    </v-footer>
  </v-app>
</template>

<script>

export default {
  name: 'App',
};
</script>
