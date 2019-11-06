<template lang="pug">
  v-layout(wrap)
    v-flex.pa-3(xs2 style="background-color:white;")
      .headline.pb-3 Products...
      v-hover(v-slot:default="{ hover }" v-for="product in products" :key="product.it")
        v-card.mb-3(:elevation="hover ? 5 : 1")
          v-img(
            class="white--text align-end"
            height="200px"
            :src="product.image"
          )
          v-card-title {{ product.name }}
          v-card-subtitle {{ product.description }}

</template>

<script>

export default {
  name: 'Home',

  data: () => ({
    products: [
      {
        id: 1,
        name: "Pomodori",
        description: "Freschi",
        image: "https://boygeniusreport.files.wordpress.com/2019/05/capture-2.png?w=782"
      },
      {
        id: 2,
        name: "Patate",
        description: "",
        image: "https://lorenzovinci.it/magazine/wp-content/uploads/2015/04/images_Bacche_di_gioia_patate.1024x768.jpg"
      },
      {
        id: 3,
        name: "Zucchine",
        description: "",
        image: "https://www.salepepe.it/files/2014/12/zucchine.jpg"
      }
    ]
  })
};
</script>
