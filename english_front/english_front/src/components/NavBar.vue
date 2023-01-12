<template>
  <v-container fluid>
    <v-app-bar color="indigo lighten-1" dark app clipped-left>

      <v-toolbar-title>ENGLISH TRAINER</v-toolbar-title>

<!--      <v-spacer/>-->
<!--      <v-btn icon @click="getAuthenticationApi">-->
<!--        <v-icon>mdi-account</v-icon>-->
<!--      </v-btn>-->
    </v-app-bar>

    <v-navigation-drawer  app clipped permanent expand-on-hover mini-variant mini-variant-width=50 width=220>
      <v-list nav dense>
        <v-list-item-group
            v-model="group"
            active-class="indigo lighten-4"
        >

          <router-link to="/">
            <v-list-item>
              <v-list-item-icon>
                <v-icon>mdi-home</v-icon>
              </v-list-item-icon>
              <v-list-item-title>Реестр слов</v-list-item-title>
            </v-list-item>
          </router-link>

          <router-link to="/debtor">
            <v-list-item>
              <v-list-item-icon>
                <v-icon>mdi-card-account-details</v-icon>
              </v-list-item-icon>
              <v-list-item-title>Карточка должника</v-list-item-title>
            </v-list-item>
          </router-link>

          <router-link to="/payments">
            <v-list-item>
              <v-list-item-icon>
                <v-icon>mdi-cash-multiple</v-icon>
              </v-list-item-icon>
              <v-list-item-title>Платежи</v-list-item-title>
            </v-list-item>
          </router-link>

          <router-link to="/mail">
            <v-list-item>
              <v-list-item-icon>
                <v-icon>mdi-email-sync</v-icon>
              </v-list-item-icon>
              <v-list-item-title>Почта</v-list-item-title>
            </v-list-item>
          </router-link>

          <router-link to="/library">
            <v-list-item>
              <v-list-item-icon>
                <v-icon>mdi-library</v-icon>
              </v-list-item-icon>
              <v-list-item-title>Библиотека</v-list-item-title>
            </v-list-item>
          </router-link>

          <router-link to="/statistics">
            <v-list-item>
              <v-list-item-icon>
                <v-icon>mdi-finance</v-icon>
              </v-list-item-icon>
              <v-list-item-title>Статистика</v-list-item-title>
            </v-list-item>
          </router-link>


        </v-list-item-group>
      </v-list>

    </v-navigation-drawer>
  </v-container>
</template>

<script>

export default {
  name: "NavBar",
  data: () => ({
    group: null,

  }),
}

</script>

<style scoped>


</style>