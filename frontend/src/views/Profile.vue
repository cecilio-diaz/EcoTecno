<template lang="pug">
    v-container
        v-card.pa-5
            v-layout
                v-flex(xs2)
                    v-avatar(size="170")
                        img(:src="'https://i.pravatar.cc/150?img=10'" )
                v-flex(xs5)
                    div(style="font-size:3rem")
                        | {{ profile.name }}
                        template(v-if="profile.verified") 
                        v-icon(large right color="blue") mdi-check
                    .subtitle.ml-2 Milano
                    div
                        v-rating(v-model="profile.rating" readonly half-increments)
                    .mt-3
                        v-btn.secondary
                            v-icon(left) mdi-message
                            | Messaggi (2)
                v-flex.text-right(xs5)
                    //img.elevation-1(src="/map.png" height="250rem")
        v-card.mt-5.pa-5
            v-layout  
                v-flex(xs12)  
                    .headline Richieste
                    v-layout.mt-3.elevation-1.pa-3(v-for="order in profile.orders.filter(x => !x.checked)" :key="order.id")
                        v-flex(xs8)
                            span(style="font-size:1.5rem") {{ order.products }}
                            span &nbsp;da <a href="#">{{ order.from }}</a>
                        v-flex.text-right(xs4)
                            v-btn.success(@click="order.checked=true")
                                v-icon(left) mdi-check
                                | Approva
                            v-btn.error.ml-3(@click="order.checked=true")
                                v-icon mdi-close
        v-card.px-5.mt-5
            v-layout(row wrap) 
                v-flex(xs12)
                    .headline.mt-4 Prodotti disponibili
                        v-btn(icon)
                            v-icon mdi-pencil
                    v-layout.pa-3(row wrap)
                        v-flex.elevation-1.mb-2(xs6 v-for="product in profile.products" :key="product.name")
                            v-layout.ma-0.px-3.py-1(row)
                                v-flex(xs2)
                                    v-avatar(size="64")
                                        img(:src="product.image")
                                v-flex(xs8)
                                    .headline {{ product.name }} x {{Math.floor(Math.random() * 10) + 1 }}Kg
                                    .subtitle {{ product.description }}
        v-card.px-5.mt-5
            v-layout(row wrap) 
                v-flex(xs12)
                    .headline.mt-4.mb-3 Monitoraggio Sensori IoT
                    v-alert.yellow.lighten-2
                        span Ti consigliamo di ridurre l'umidità del tuo orto per migliorare la produzione
                    
                    v-layout.mt-3(row wrap)
                        template(v-for="device in profile.devices")
                            v-flex.pa-4(xs4)
                                LineChart(:chartdata="makeChartData(device.data, device.name)")
            
</template>

<script>
import LineChart from '../components/LineChart'

export default {
    components: { LineChart },
    methods: {
        makeChartData(sensorData, name) {
            const average = arr => arr.reduce( ( p, c ) => p + c, 0 ) / arr.length;
            const data = {
                labels: sensorData.map((x,i) => i),
                datasets: [{
                    label: name,
                    data: sensorData,
                    pointBackgroundColor: 'rgba(73, 184, 110, 0.5)',
                    backgroundColor: 'rgba(73, 184, 110, 0.5)'
                },
                {
                    pointBackgroundColor: 'rgba(73, 184, 110, 0.9)',
                    backgroundColor: 'rgba(255, 184, 110, 0.9)',
                    label: "",
                    fill: false,
                    data: sensorData.map(() => average(sensorData)),  //array [1,2,3,4,5,6,7]         
                }]
            }
            return data
        }
    },
    data: () => ({
        profile: {
            name: "Martina Verdi",
            verified: true,
            rating: 4.5,
            orders: [
                {
                    id: 1,
                    from: "Matteo Romolo",
                    products: "3Kg Pomodori, 2Kg Cipolle",
                    checked: false
                },
                {
                    id: 2,
                    from: "Federica Abete",
                    products: "2Kg Patate, 500g Basilico",
                    checked: false
                }
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
            ],
            devices: [{
                name: 'Temperatura Pomodori',
                data: [31,28,32,27,28]
            },
            {
                name: 'Irrigazione Zucchine',
                data: [9, 8, 11, 15, 3]
            },
            {
                name: 'CO2 Aria',
                data: [7, 7, 7, 15, 2, 8]
            },
            {
                name: 'Umidità Terreno',
                data: [9,9,9,9,8,9]
            }]
        }
    })
    
}
</script>