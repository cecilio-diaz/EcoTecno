<template lang="pug">
v-app
  v-app-bar(app color='primary' dark)
    router-link.d-flex.align-center.justify-center(:to="{name:'home'}" style="color:white;text-decoration:none")
      v-icon(left) mdi-spa
      v-toolbar-title
        | BlaBlaFarm
    v-spacer
    v-btn.mr-1(:to='{ name: "home" }' text exact)
      v-icon(left) mdi-map-outline
      span Prodotti
    v-btn.mr-1(:to='{ name: "recipes" }' text exact)
      v-icon(left) mdi-silverware-fork-knife
      span Ricette
    v-btn.mr-1(:to='{ name: "profile" }' text exact)
      v-icon(left) mdi-sprout
      span Il tuo orto
    //v-btn.mr-1(:to='{ name: "profile" }' text)
    v-avatar(size="36").mx-3
      img( src="https://i.pravatar.cc/150?img=10")
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
