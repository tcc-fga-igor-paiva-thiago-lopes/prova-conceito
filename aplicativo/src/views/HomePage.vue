<template>
  <ion-page>
    <ion-header :translucent="true">
      <ion-toolbar>
        <ion-title>Viagens</ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content :fullscreen="true">
      <!-- <ion-refresher slot="fixed" @ionRefresh="refresh($event)">
        <ion-refresher-content></ion-refresher-content>
      </ion-refresher> -->

      <ion-header collapse="condense">
        <ion-toolbar>
          <ion-title size="large">Viagens</ion-title>
        </ion-toolbar>
      </ion-header>

      <ion-list>
        <!-- <MessageListItem v-for="message in messages" :key="message.id" :message="message" /> -->
        <p v-for="trip in trips" :key="trip.id">
          {{trip.text}}
        </p>
      </ion-list>
    </ion-content>
  </ion-page>
</template>

<script lang="ts">
import {
  IonContent,
  IonHeader,
  IonList,
  IonPage,
  // IonRefresher,
  // IonRefresherContent,
  IonTitle,
  IonToolbar,
} from '@ionic/vue';

export default {
  data(): {
    trips: {id: number, text: string}[],
  } {
    return {
      trips: [],
    };
  },
  created() {
    const apiBaseUrl = process.env.VUE_APP_API_URL || 'http://localhost:5001';

    fetch(`${apiBaseUrl}/trips`)
      .then((response) => response.json())
      .then((data) => {
        console.log(data);

        this.trips = data.list;
      })
      .catch((error) => {
        console.log(error);
      });
  },
  mounted() {
    console.log('trips: ', this.trips);
  },
  methods: {
  }
};
</script>
