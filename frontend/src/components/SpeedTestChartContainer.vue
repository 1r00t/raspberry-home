<template>
  <div class="container">
    <speed-test-chart
      v-if="loaded"
      :chartdata="chartdata"
      :options="options"/>
  </div>
</template>

<script>
import SpeedTestChart from './SpeedTestChart.vue'

export default {
  name: 'SpeedTestChartContainer',
  components: { SpeedTestChart },
  data: () => ({
    loaded: false,
    chartdata: null,
    options: null,
    labels: [],
    datasets: [],
    baseUrl: process.env.VUE_APP_SPEEDTEST_URL,
  }),
  async mounted () {
    this.loaded = false

    try {
      await this.axios
            .get(this.baseUrl)
            .then(response => (
              this.labels = response.data.labels,
              this.datasets = response.data.datasets
            ));

      this.chartdata = {
          labels: this.labels,
          datasets: this.datasets,
          backgroundColor: ["red", "blue"],
      }
      this.options = {
        scales: {
          xAxes: [{
            type: "time",
            distribution: "series",
            ticks: {
              autoSkip: true,
              maxTicksLimit: 10,
            },
            scaleLabel: {
              display: true,
              labelString: "Times measured"
            }
          }],
          yAxes: [{
            scaleLabel: {
              display: true,
              labelString: "Mbit/s"
            }
          }]
        }
      }
      this.loaded = true
    } catch (e) {
      console.error(e)
    }
  }
}
</script>
