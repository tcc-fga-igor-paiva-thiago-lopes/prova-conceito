<template>
    <ion-page>
      <ion-header :translucent="true">
        <ion-toolbar>
          <ion-title>Cadastro</ion-title>
        </ion-toolbar>
      </ion-header>
  
      <ion-content :fullscreen="true">
        <div v-if="loading">
          <ion-loading />
        </div>

        <form class="form">
            <ion-list style="padding: 0">
                <ion-item class="form-item">
                    <ion-label position="stacked">Nome *</ion-label>
                    <ion-input
                        required
                        :name="name"
                        v-model="name"
                        placeholder="Digite seu nome"
                    >
                    </ion-input>
                </ion-item>

                <ion-item class="form-item">
                    <ion-label position="stacked">E-mail *</ion-label>
                    <ion-input
                        required
                        type="email"
                        inputmode="email"
                        :name="email"
                        v-model="email"
                        placeholder="Digite seu e-mail"
                    >
                    </ion-input>
                    <ion-note slot="helper">Insira um e-mail válido</ion-note>
                    <ion-note slot="error">E-mail inválido</ion-note>
                </ion-item>

                <ion-item class="form-item">
                    <ion-label position="stacked">Senha *</ion-label>
                    <ion-input
                        required
                        type="password"
                        :name="password"
                        v-model="password"
                        placeholder="Digite sua senha"
                    >
                    </ion-input>
                </ion-item>

                <ion-item class="form-item">
                    <ion-label position="stacked">Confirmação de senha *</ion-label>
                    <ion-input
                        required
                        type="password"
                        placeholder="Confirme sua senha"
                        :name="password_confirmation"
                        v-model="password_confirmation"
                    >
                    </ion-input>
                    <ion-note slot="helper">Deve ser igual a senha</ion-note>
                </ion-item>

                <ion-text color="danger" v-if="!loading && errorMessage">
                    <h6>{{errorMessage}}</h6>
                </ion-text>
            </ion-list>

            <ion-button shape="round" :onclick="submit" style="margin-top: 16px">
                Criar conta
            </ion-button>
        </form>
      </ion-content>
    </ion-page>
  </template>
  
  <style>
  .form {
    display: flex;
    padding: 16px;
    flex-direction: column;
  }

  .form-item {
    margin: 8px 0;
  }
  </style>
  
  <!-- lang="ts" -->
  <script>
  import axios from 'axios';

  import {
    IonContent,
    IonHeader,
    IonPage,
    IonTitle,
    IonToolbar,
    IonText,
    IonLoading,
    IonInput,
    IonButton,
    IonList,
    IonNote,
    IonItem,
    IonLabel,
    toastController
  } from '@ionic/vue';
  
  export default {
    data() {
      return {
        loading: false,
        errorMessage: '',
        name: '',
        email: '',
        password: '',
        password_confirmation: '',
        isToastOpen: true,
        toastMessage: 'Ahuaskjdhasjkdh'
      };
    },
    methods: {
        async presentToast(message, color, position = 'top') {
            const toast = await toastController.create({
                message,
                position,
                color,
                duration: 1500,
            });

            await toast.present();
        },
        submit() {
            // const apiBaseUrl = process.env.VUE_APP_API_URL || 'https://prova-conceito.herokuapp.com';

            const apiBaseUrl = 'http://localhost:5000'
            
            const { name, email, password, password_confirmation } = this;

            console.log({
                name, email, password, password_confirmation
            })
            
            if (!name || !email || !password|| !password_confirmation) {
                this.errorMessage = 'Todos os campos com * são obrigatórios';
                return;
            }

            if (password != password_confirmation) {
                this.errorMessage = 'A senha e confirmação de senha devem ser iguais';
                return;
            }

            this.loading = true;

            axios
                .post(`${apiBaseUrl}/truck_driver`, {
                    name,
                    email,
                    password,
                    password_confirmation,
                })
                .then((response) => {
                    console.log(response);
                    this.errorMessage = '';
                    this.presentToast('Conta criada com sucesso!', 'success');
                    this.$router.push({ name: 'Home' })
                })
                .catch((error) => {
                    console.error(error);
                    this.errorMessage = error.response.data.error;
                    this.presentToast(this.errorMessage, 'danger');
                })
                .finally(() => {
                    this.loading = false;
                });
        },
    },
    components: {
      IonContent,
      IonHeader,
      IonPage,
      IonTitle,
      IonToolbar,
      IonText,
      IonLoading,
      IonInput,
      IonButton,
      IonList,
      IonNote,
      IonItem,
      IonLabel
    },
  }
  </script>
  