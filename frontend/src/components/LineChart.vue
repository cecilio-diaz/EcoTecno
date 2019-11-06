<script>
import { Line } from 'vue-chartjs'

export default {
  extends: Line,
  props: {
    chartdata: { required: true },
    options: {
        default: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    } 
  },
  mounted () {
    this.renderChart(this.chartdata, this.options)
  }
}
</script>