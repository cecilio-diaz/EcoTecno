<template lang="pug">
v-app
  v-app-bar(app color='primary' dark)
    .d-flex.align-center
      v-toolbar-title EcoTecno Idea
    v-spacer
    // v-btn(href='https://github.com/vuetifyjs/vuetify/releases/latest' target='_blank' text)
      span.mr-2 Latest Release
      v-icon mdi-open-in-new
  v-content
    router-view
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    //
  }),
};
</script>
