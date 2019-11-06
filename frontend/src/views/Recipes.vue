<template lang="pug">
  v-layout(wrap style="height:100vh")
    v-flex.pa-3(xs3 style="overflow:auto;" fill-height)
      v-hover(v-slot:default="{ hover }" v-for="recipe in recipes" :key="recipe.id")
        v-card.mb-3(:elevation="hover ? 5 : 1" @click="selectedRecipe=recipe.id")
          v-img(
            class="white--text align-end"
            height="200px"
            :src="recipe.image"
          )
          v-card-title {{ recipe.name }}
          v-card-subtitle {{ recipe.description }}
    v-flex(xs9 ref="mapContainer")
      template(v-if="selectedRecipe")
        GmapMap(
          :center="{lat:45.4642, lng:9.1900}"
          :zoom="10"
          :style="{ width: mapWidth + 'px', height: mapHeight + 'px' }"
          :options="mapOptions"
        )
          template(v-if="selectedRecipe")
            GmapMarker(
              :key="index"
              v-for="(seller, index) in sellers[selectedRecipe]"
              :position="seller.position"
              :clickable="true"
              @click="center=seller.position"
            )
      template(v-else)
        .d-flex.align-center.text-center(style="height:100%;background-color:white")
          v-flex()
            .subtitle Choose a product on the left
</template>

<script>

export default {
  name: 'Home',

  mounted() {
    this.mapWidth = this.$refs.mapContainer.offsetWidth;
    this.mapHeight = this.$refs.mapContainer.offsetHeight;
  },
  data: () => ({
    mapWidth: 100,
    mapHeight: 300,
    selectedRecipe: null,
    mapOptions: {
      styles: [
        {
            "featureType": "landscape",
            "stylers": [
                {
                    "hue": "#FFBB00"
                },
                {
                    "saturation": 43.400000000000006
                },
                {
                    "lightness": 37.599999999999994
                },
                {
                    "gamma": 1
                }
            ]
        },
        {
            "featureType": "road.highway",
            "stylers": [
                {
                    "hue": "#FFC200"
                },
                {
                    "saturation": -61.8
                },
                {
                    "lightness": 45.599999999999994
                },
                {
                    "gamma": 1
                }
            ]
        },
        {
            "featureType": "road.arterial",
            "stylers": [
                {
                    "hue": "#FF0300"
                },
                {
                    "saturation": -100
                },
                {
                    "lightness": 51.19999999999999
                },
                {
                    "gamma": 1
                }
            ]
        },
        {
            "featureType": "road.local",
            "stylers": [
                {
                    "hue": "#FF0300"
                },
                {
                    "saturation": -100
                },
                {
                    "lightness": 52
                },
                {
                    "gamma": 1
                }
            ]
        },
        {
            "featureType": "water",
            "stylers": [
                {
                    "hue": "#0078FF"
                },
                {
                    "saturation": -13.200000000000003
                },
                {
                    "lightness": 2.4000000000000057
                },
                {
                    "gamma": 1
                }
            ]
        },
        {
            "featureType": "poi",
            "stylers": [
                {
                    "hue": "#00FF6A"
                },
                {
                    "saturation": -1.0989010989011234
                },
                {
                    "lightness": 11.200000000000017
                },
                {
                    "gamma": 1
                }
            ]
        }
      ],
    },
    recipes: [
      {
        id: 1,
        name: "Pasta ai Pomodorini Pachino",
        description: "Piatto di stagione",
        image: "https://boygeniusreport.files.wordpress.com/2019/05/capture-2.png?w=782",
        ingredients: [
            {lat:45.4642, lng:9.1900},
        ]
      },
      {
        id: 2,
        name: "Risotto di Zucchine",
        description: "Vicino a te",
        image: "https://lorenzovinci.it/magazine/wp-content/uploads/2015/04/images_Bacche_di_gioia_patate.1024x768.jpg",
        ingredients: [
            {lat:45.4642, lng:9.1900},
        ]
      },
      {
        id: 2,
        name: "Zucca al Forno",
        description: "Piatto del Novembre",
        image: "https://lorenzovinci.it/magazine/wp-content/uploads/2015/04/images_Bacche_di_gioia_patate.1024x768.jpg",
        ingredients: [
            {lat:45.4642, lng:9.1900},
        ]
      }
    ]
  })
};
</script>
