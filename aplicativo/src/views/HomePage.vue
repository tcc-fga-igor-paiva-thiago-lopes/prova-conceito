<template>
  <ion-page>
    <ion-header :translucent="true">
      <ion-toolbar>
        <ion-title>Página inicial</ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content :fullscreen="true">
      <div class="options-container">
        <ion-text>
          <h5>Bem-vindo!</h5>
        </ion-text>

        <ion-button
          shape="round"
          class="signup-button"
          :onclick="() => $router.push({ name: 'SignUp' })"
        >
          Criar conta
        </ion-button>
      </div>
    </ion-content>
  </ion-page>
</template>

<style>
.options-container {
  width: 100%;
  display: flex;
  padding-top: 32px;
  align-items: center;
  flex-direction: column;
  justify-content: space-between;
}

.signup-button {
  width: 250px;
  margin-top: 32px;
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
  IonText,
  ionButton,
} from '@ionic/vue';

export default {
  data() {
    return {

    };
  },
  components: {
    IonContent,
    IonHeader,
    IonPage,
    IonTitle,
    IonToolbar,
    IonText,
    ionButton,
  },
}
</script>
