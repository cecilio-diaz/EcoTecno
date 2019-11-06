<template lang="pug">
  v-container
    v-card.pa-5
        v-layout
            v-flex(xs2)
                v-avatar(size="170")
                    img(:src="profile.image")
            v-flex(xs5)
                div(style="font-size:3rem")
                    | {{ profile.profile }}
                    template(v-if="profile.verified") 
                    v-icon(large right color="blue") mdi-check
                .subtitle.ml-2 Milano
                div
                    v-rating(v-model="profile.rating" readonly half-increments)
                .mt-3
                    v-btn.secondary
                        v-icon(left) mdi-message
                        | Contatta
            v-flex.text-right(xs5)
                img.elevation-1(src="/map.png" height="250rem")
        v-container(grid-list-lg v-if="!orderSent") 
            hr.my-3
            v-layout.pa-3(row wrap)
                v-flex.elevation-1.mb-2(xs6 v-for="product in profile.products" :key="product.name")
                    v-layout(row wrap)
                        v-flex(xs2)
                            v-avatar(size="64")
                                img(:src="product.image")
                        v-flex(xs8)
                            .headline {{ product.name }}
                            .subtitle {{ product.description }}
                        v-flex.text-right(xs2)
                            v-text-field.ma-0(type="number" style="width:10rem" placeholder="Qtà" append-icon="mdi-scale" min="1")
            v-layout
                v-textarea(placeholder="Aggiungi un commento alla richiesta")
            v-layout
                v-btn.accent(block big @click="orderSent=true")
                    v-icon(left) mdi-cart
                    | Richiedi Disponibilità  
        v-container(v-else)
            v-alert(color="primary" dark)
                .headline.text-center Richiesta inviata! 
    v-card.mt-3
        v-container(grid-list-lg)
            .headline Aggiornamenti dall'orto...
            v-layout.pa-3(row wrap)
                v-flex.elevation-1.mr-3(xs3 v-for="update in profile.updates" :key="update.url")
                    v-layout(row wrap)
                        v-flex(xs12)
                            .subtitle {{ update.title }}
                            v-img(:src="update.url" height="10rem")

</template>

<script>
import Profile from '../api/Profile'
export default {
    name: "Order",
    async mounted() {
        const profile = await Profile.get(this.$route.params.id);
        this.profile = {...profile, ...this.profile}
        console.log(this.profile)
    },
    data: () => ({
        orderSent: false,
        profile: {
            name: "Laura Rossi",
            verified: true,
            rating: 4.5,
            updates: [
                {   
                    title: 'In coltivazione...',
                    url: 'https://images.barrons.com/im-76867?width=620&size=1.5'
                },
                {   
                    title: 'Raccolto di ieri',
                    url: 'https://media.istockphoto.com/photos/basket-of-fresh-garden-produce-and-vegetable-in-field-picture-id537666129'
                },
            ],
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
                    name: "Cetrioli",
                    description: "",
                    image: "https://galleria.riza.it/files/article/cetrioli-combattono-la-ritenzione-idrica-e-l-accumulo-di-grassi.jpg"
                },
            ]
        }    
    })
}
</script>