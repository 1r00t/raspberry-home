<template>
  <!-- <div class="speedtest">
    <h1>Speedtest</h1>
    <h2>Status: <b-badge :variant="enabledvariant">{{ is_enabled ? "enabled": "disabled"}}</b-badge></h2>
    <div>
      <b-button-group>
        <b-button @click="startSpeedTest()">Start</b-button>
        <b-button @click="stopSpeedTest()">Stop</b-button>
      </b-button-group>
    </div>
  </div> -->

  <div class="speedtest">
    <b-row>
      <b-col cols="4">
        <b-card-group deck>
          <b-card header="Speedtest Settings" header-tag="header">
            <!-- <b-card-title>Speedtest</b-card-title> -->
            <b-card-text>Test the speed every <b>x</b> minutes</b-card-text>
            <b-input-group :append="minutes + ' minutes'">
              <b-input-group-prepend is-text>
                <b-form-checkbox switch class="mr-n2" v-model="check_enabled">
                  <span class="sr-only">Switch for following text input</span>
                </b-form-checkbox>
              </b-input-group-prepend>
              <b-form-input
                id="minutes-1"
                v-model="minutes"
                type="range"
                min="1"
                max="60"
              ></b-form-input>
            </b-input-group>
          </b-card>
        </b-card-group>
      </b-col>
      <b-col cols="8">
        <b-card-group deck>
          <b-card header="Measured speed" header-tag="header">
            <SpeedTestChartContainer></SpeedTestChartContainer>
          </b-card>
        </b-card-group>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import SpeedTestChartContainer from "@/components/SpeedTestChartContainer.vue";
export default {
  name: "SpeedTest",
  components: { SpeedTestChartContainer },
  data() {
    return {
      is_enabled: null,
      check_enabled: null,
      //enabledvariant: "secondary",
      baseUrl: process.env.VUE_APP_SPEEDTEST_URL,
      minutes: 2
    };
  },

  methods: {
    toggleSpeedTest() {
      console.log("BLALALALALALALALA")
      if (this.is_enabled) {
        this.stopSpeedTest();
      } else {
        this.startSpeedTest();
      }
    },
    startSpeedTest() {
      this.axios
        .post(this.baseUrl, {
          job: "start",
          minutes: this.minutes
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
        this.check_enabled = true;
      } else {
        this.check_enabled = false;
      }
    },
    check_enabled: function(val) {
      if (val && !this.is_enabled) {
        console.log("START TEST");
        this.startSpeedTest();
      } else if(!val && this.is_enabled) {
        console.log("STOP TEST");
        this.stopSpeedTest();
      }
    }
  },

  mounted() {
    this.axios
      .get(this.baseUrl)
      .then(response => (
        this.is_enabled = response.data.is_enabled,
        this.minutes = response.data.minutes
      )
    );
  }
};
</script>
