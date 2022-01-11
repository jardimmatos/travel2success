import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';
import 'vuetify/dist/vuetify.min.css'
Vue.use(Vuetify);

const opts = {
    theme: {
        themes: {
            light: {
                //primary: '#50c878', 
                //secondary: colors.red.lighten4, // #FFCDD2
                //accent: colors.indigo.base, // #3F51B5
            },
        },
    },
    lang:{
        locales:{
            en:{
                dataTable:{
                    itemsPerPageText : 'Linhas por página',
                    sortDescending: 'Ordem decrescente',
                    sortAscending: 'Ordem crescente',
                    sortBy:'Ordenar por'
                }
            }
        }
    }
   
}
export default new Vuetify(opts);
