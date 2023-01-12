<template>
  <v-container fluid>

    <v-row>
      <v-data-table
          class="table elevation-1"
          v-model="selected"
          :headers="headers"
          :items="debtors"
          :single-select="singleSelect"
          :search="search"
          :page.sync="page"
          :items-per-page="itemsPerPage"
          @page-count="pageCount = $event"
          item-key="name"
          dense
          show-select
          hide-default-footer>
        <template v-slot:top>
          <v-row>
            <v-col lg="2">
              <v-switch v-model="singleSelect" label="Single select" class="pa-3"></v-switch>
            </v-col>

            <v-col lg="3">
              <v-text-field v-model="search" append-icon="mdi-magnify" label="Поиск" single-line
                            hide-details></v-text-field>
            </v-col>

            <v-col lg="2" offset-lg="1">
              <v-autocomplete
                  v-model="filterValue"
                  :items="filters"
                  label="Фильтры"
                  clearable
              ></v-autocomplete>
            </v-col>

            <v-col lg="2">
              <v-autocomplete
                  v-model="dispatchValue"
                  :items="dispatch"
                  label="Шаблоны заявлений"
                  clearable
              ></v-autocomplete>
            </v-col>

          </v-row>
        </template>
      </v-data-table>
    </v-row>

    <!--    <div>-->
    <!--      <v-btn class="botton" @click="getDebtorsApi" outlined>-->
    <!--        Получить список должников-->
    <!--      </v-btn>-->
    <!--      {{headers}}-->
    <!--      auth_token = {{ authStore.token[0] }}-->
    <!--    </div>-->

    <v-row style="width: 100%; position: absolute; bottom: 20px">
      <v-col lg="10">
        <div class="text-center pt-2">
          <v-pagination v-model="page" :length="pageCount"
          ></v-pagination>
        </div>
      </v-col>

      <v-col lg="2">
        <v-text-field
            :value="itemsPerPage"
            label="Количество строк на странице"
            type="number"
            @input="itemsPerPage = parseInt($event, 10)"
        ></v-text-field>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import {useAuthStore} from "@/stores/AuthStore";

export default {
  name: "RegistryPage",
  data() {
    return {
      authStore: useAuthStore(),
      search: '',
      singleSelect: false,
      selected: [],
      filterValue: null,
      dispatchValue: null,
      page: 1,
      pageCount: 0,
      itemsPerPage: 5,
      filters: [
        'Фильтр 1',
        'Фильтр 2',
        'Фильтр 3',
        'Фильтр 4',
      ],
      dispatch: [
        'Шаблон 1',
        'Шаблон 2',
        'Шаблон 3',
        'Шаблон 4',
      ],
      headers: [],
      debtors: [],
    }
  },

  mounted() {
    this.getDebtorsApi()
  },
  methods: {
    getDebtorsApi() {
      const auth_token = this.authStore.token[0]

      this.axios.get('http://localhost:8000/api/v1/getHeaders/', {headers: {"Authorization": `Token ${auth_token}`},})
          .then(response => this.headers = response.data)

      this.axios.get('http://localhost:8000/api/v1/getDebtorsRegistry/', {headers: {"Authorization": `Token ${auth_token}`},})
          .then(response => this.debtors = response.data)
    },
  }
}


</script>

<style scoped>

</style>