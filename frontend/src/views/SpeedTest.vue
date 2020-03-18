<template>
  <div class="speedtest">
    <h1>Speedtest</h1>
    <h2>Status: <b-badge :variant="enabledvariant">{{ is_enabled ? "enabled": "disabled "}}</b-badge></h2>
    <div>
      <b-button-group>
        <b-button @click="startSpeedTest()">Start</b-button>
        <b-button @click="stopSpeedTest()">Stop</b-button>
      </b-button-group>
    </div>
  </div>
</template>

<script>
export default {
  name: "SpeedTest",
  data() {
    return {
      is_enabled: null,
      enabledvariant: "secondary",
      baseUrl: process.env.VUE_APP_SPEEDTEST_URL
    };
  },
  methods: {
    startSpeedTest() {
      this.axios
        .post(this.baseUrl, {
          job: "start",
          minutes: 2
        })
        .then(response => (this.is_enabled = response.data.is_enabled));
    },
    stopSpeedTest() {
      this.axios
        .post(this.baseUrl, {
          job: "stop"
        })
        .then(response => (this.is_enabled = response.data.is_enabled));
    }
  },
  watch: {
    is_enabled: function(val) {
      if (val) {
        this.enabledvariant = "success";
      } else {
        this.enabledvariant = "danger";
      }
    }
  },
  mounted() {
    console.log("#############: " + this.baseUrl)
    this.axios
      .get(this.baseUrl)
      .then(response => (this.is_enabled = response.data.is_enabled));
  }
};
</script>
