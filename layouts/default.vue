<template>
  <v-app>
    <v-navigation-drawer v-model="drawer" :mini-variant="miniVariant" :clipped="clipped" fixed app temporary>
      <v-list>
        <v-list-item v-for="(item, i) in items" :key="i" :to="item.to" router exact class="bordered-item">
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <!--------------------------------- Nav bar ---------------------------- -->
    <v-app-bar class=" red darken-4" :clipped-left="clipped" fixed app>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title class="text-h3 white--text font-weight-medium">{{ title }}</v-toolbar-title>
      <v-spacer />
      <v-btn icon rightDrawer >
        <v-icon>mdi-logout</v-icon>
      </v-btn>
    </v-app-bar>
    <!-- --------------------------------------------------------------------- -->
    <v-main>
      <v-container >
        <Nuxt />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'DefaultLayout',

  data() {
    return {
      clipped: false,
      drawer: false,
      fixed: false,
      items: [

        {
          icon: 'mdi-home',
          title: 'Home',
          to: '/fullcalendar'
        },
        {
          icon: 'mdi-calendar-plus',
          title: 'Create meet',
          to: '/create'
        },
        {
          icon: 'mdi-calendar',
          title: 'All meet',
          to: '/fullcalendar'
        }
        //----- icon source:https://pictogrammers.github.io/@mdi/font/3.6.95/

      ],
      miniVariant: false,
      right: true,
      rightDrawer: false,
      title: 'Jmeet'
    }
  },
  watch: {
    group() {
      this.drawer = false
    },
  },
}
</script>
