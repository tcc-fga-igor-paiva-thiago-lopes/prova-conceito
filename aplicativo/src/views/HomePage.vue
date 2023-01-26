<template>
  <ion-page>
    <ion-header :translucent="true">
      <ion-toolbar>
        <ion-title>Viagens</ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content :fullscreen="true">
      <ion-header collapse="condense">
        <ion-toolbar>
          <ion-title size="large">Viagens</ion-title>
        </ion-toolbar>
      </ion-header>

      <div v-if="loading">
        <IonLoading />
      </div>

      <div v-if="!loading">
        <IonCard v-for="trip in trips" :key="trip.id">
          <IonCardHeader class="trip-card-header">
            {{trip.description}}
          </IonCardHeader>

          <IonCardContent>
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
          </IonCardContent>
        </IonCard>
      </div>
    </ion-content>
  </ion-page>
</template>

<!-- lang="ts" -->
<script>
import {
  IonCard,
  IonCardContent,
  IonCardHeader,
  IonContent,
  IonHeader,
  IonLoading,
  IonPage,
  IonTitle,
  IonToolbar,
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
      trips: [], // as Trip[],
    };
  },
  created() {
    const apiBaseUrl = process.env.VUE_APP_API_URL || 'http://localhost:5001';
    // const apiBaseUrl = 'http://localhost:5001';

    this.loading = true;

    fetch(`${apiBaseUrl}/trips`)
      .then((response) => response.json())
      .then((data) => {
        console.log('request data: ', data);
        console.log('request data list: ', data.list);
        this.trips = [...data.list]; // as Trip[];
      })
      .catch((error) => {
        console.log(error);
      })
      .finally(() => {
        this.loading = false;
      });
  },
  components: { IonLoading, IonCard, IonCardHeader, IonCardContent }
};
</script>

<style scoped>
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
