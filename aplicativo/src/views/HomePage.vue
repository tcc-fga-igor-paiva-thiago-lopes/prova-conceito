<template>
  <ion-page>
    <ion-header :translucent="true">
      <ion-toolbar>
        <ion-title>Viagens</ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content :fullscreen="true">
      <div v-if="loading">
        <ion-loading />
      </div>

      <div v-if="!loading && !loadSuccessful">
        <ion-text color="danger">
          <h5>Falha ao carregar as viagens...</h5>
        </ion-text>
      </div>

      <div v-if="!loading && loadSuccessful">
        <ion-card v-for="trip in trips" :key="trip.id">
          <ion-card-header class="trip-card-header">
            {{trip.description}}
          </ion-card-header>

          <ion-card-content>
            <div class="pair-trip-container">
              <span><strong>Origem: </strong> {{ trip.origin }}</span>
              <span><strong>Destino: </strong> {{ trip.destination }}</span>
            </div>

            <div class="pair-trip-container" style="margin-top: 16px">
              <span><strong>Distância: </strong> {{ `${trip.distance} km` }}</span>
              <span><strong>Tipo de carga: </strong> {{ trip.cargo_type }}</span>
            </div>

            <div class="pair-trip-container" style="margin-top: 16px">
              <span><strong>Peso carga: </strong> {{ `${trip.cargo_weight} kg` }}</span>
              <span><strong>Contratante: </strong> {{ trip.company }}</span>
            </div>

            <div class="pair-trip-container" style="margin-top: 16px">
              <span><strong>Início: </strong> {{ trip.start_date }}</span>
              <span><strong>Fim: </strong> {{ trip.end_date }}</span>
            </div>
          </ion-card-content>
        </ion-card>
      </div>
    </ion-content>
  </ion-page>
</template>

<style>
.pair-trip-container {
  display: flex;
  justify-content: space-between;
}

.trip-card-header {
  margin: 0 auto;
  font-size: 20px;
  font-weight: bold;
  width: fit-content;
}
</style>

<!-- lang="ts" -->
<script>
import {
  IonContent,
  IonHeader,
  IonPage,
  IonTitle,
  IonToolbar,
  IonCard,
  ionText,
  IonCardHeader,
  IonCardContent,
} from '@ionic/vue';

// interface Trip {
//   id: number;
//   origin: string;
//   destination: string;
//   distance: number;
//   cargo_type: string;
//   cargo_weight: number;
//   start_date: string;
//   end_date: string;
//   description: string;
//   company: string;
// }

export default {
  data() {
    return {
      loading: false,
      loadSuccessful: true,
      trips: [] // as Trip[],
    };
  },
  created() {
    const apiBaseUrl = process.env.VUE_APP_API_URL || 'https://prova-conceito.herokuapp.com';

    fetch(`${apiBaseUrl}/trips`)
      .then((response) => response.json())
      .then((data) => {
        console.log('request data: ', data);
        console.log('request data list: ', data.list);

        this.trips = [...data.list]; // as Trip[];

        this.loadSuccessful = true;
      })
      .catch((error) => {
        console.log(error);
        this.loadSuccessful = false;
      })
      .finally(() => {
        this.loading = false;
      });
  },
  components: {
    IonContent,
    IonHeader,
    IonPage,
    IonTitle,
    IonToolbar,
    IonCard,
    ionText,
    IonCardHeader,
    IonCardContent,
  },
}
</script>
