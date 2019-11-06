<template lang="pug">
  v-layout(wrap style="height:100vh")
    v-flex.pa-3(xs2 style="overflow:auto;" fill-height)
      v-hover(v-slot:default="{ hover }" v-for="product in products" :key="product.id")
        v-card.mb-3(:elevation="hover ? 5 : 1" @click="selectedProduct=product.id")
          v-img(
            class="white--text align-end"
            height="200px"
            :src="product.image"
          )
          v-card-title {{ product.product }}
          v-card-subtitle {{ product.description }}
    v-flex.pa-3(xs2 style="background-color:white;overflow:auto;" fill-height)
      div(v-if="findSellers(selectedProduct).length" v-for="seller in findSellers(selectedProduct)" :key="seller.id")
        v-card.mb-3(:to="{ name: 'order', params : { id: seller.id } }")
          v-layout(align-center)
            v-flex.text-center(xs3)
              v-avatar
                v-img(:src="seller.image")
            v-flex(xs9)
              v-card-title
                | {{ seller.profile }}
                template(v-if="seller.verified") 
                  v-icon(right small color="blue") mdi-check
              v-card-subtitle.pb-0 Disponibile {{ Math.floor(Math.random() * 10) + 1 }}Kg
              v-rating.pl-3.pb-3(v-model="seller.rating" readonly small dense half-increments) 
    v-flex(xs8 ref="mapContainer")
      template(v-if="selectedProduct")
        GmapMap(
          :center="{lat:45.4642, lng:9.1900}"
          :zoom="10"
          :style="{ width: mapWidth + 'px', height: mapHeight + 'px' }"
          :options="mapOptions"
        )
          template(v-if="selectedProduct")
            GmapMarker(
              :key="index"
              v-for="(seller, index) in findSellers(selectedProduct)"
              :position="{ lat: seller.latitude, lng: seller.longitude }"
              :clickable="true"
              @click="center=seller.position"
            )
      template(v-else)
        .d-flex.align-center.text-center(style="height:100%;background-color:white")
          v-flex()
            .subtitle Choose a product on the left
</template>

<script>
import Products from '../api/Products'
import Profile from '../api/Profile'

export default {
  name: 'Home',

  async mounted() {
    this.mapWidth = this.$refs.mapContainer.offsetWidth;
    this.mapHeight = this.$refs.mapContainer.offsetHeight;
    this.products = (await Products.all()).results
    this.sellers = (await Profile.all()).results
    this.sellings = (await Products.sellers()).results
  },
  methods: {
    findSellers: function(product) {
      let sellers = []
      for (const selling of this.sellings) {
        if(product == selling.product) {
          const seller_id = selling.sellers[0]
          for (const seller of this.sellers) {
            if (seller.id == seller_id) {
              sellers.push(seller)
            }
          }
        }
      }
      console.log(sellers)
      return sellers;
    }
  },
  data: () => ({
    mapWidth: 100,
    mapHeight: 300,
    selectedProduct: null,
    sellings: [],
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
    sellers: {
      1: [
        {
          id: 1,
          name: "Laura Rossi",
          image: "https://i.pravatar.cc/150?img=1",
          rating: 4.5,
          position: {lat:45.4642, lng:9.1900},
          verified: true,
        },
        {
          id: 2,
          name: "Tizio Caio",
          image: "https://i.pravatar.cc/150?img=2",
          rating: 4,
          position: {lat:45.44, lng:9.0900}
        }
      ],
      2: [
        {
          id: 1,
          name: "Laura Rossi",
          rating: 4.5,
          position: {lat:45.4642, lng:9.1900},
          verified: true,
        },
        {
          id: 3,
          name: "Mario Verdi",
          rating: 5,
          position: {lat:45.30, lng:9.0900}
        }
      ]
    },
    products: [
      {
        id: 1,
        product: "Tomato",
        image: "https://images.unsplash.com/photo-1518977822534-7049a61ee0c2?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1000&q=80"
      }
    ]
  })
};
</script>
