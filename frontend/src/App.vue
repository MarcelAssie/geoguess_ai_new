<template>
  <div id="app">
    <WelcomePage
      v-if="currentPage === 'welcome'"
      @start-game="showGamePage"
      @show-rules="showRules"
    />
    <GamePage
      v-else-if="currentPage === 'game'"
      @back-to-welcome="showWelcomePage"
    />
  </div>
</template>

<script>
import WelcomePage from './components/Welcome.vue'
import GamePage from './components/GamePage.vue'

export default {
  name: 'App',
  components: {
    WelcomePage,
    GamePage
  },
  data() {
    return {
      currentPage: 'welcome'
    }
  },
  methods: {
    showGamePage() {
      this.currentPage = 'game'
    },
    showWelcomePage() {
      this.currentPage = 'welcome'
    },
    showRules() {
      // Vous pouvez implémenter une modal pour les règles plus tard
      alert(`Règles du jeu GeoGuessAI :
      1. Deux modes de jeu :
         - Adresse → Coordonnées : Devinez les coordonnées exactes à partir d'une adresse
         - Coordonnées → Adresse : Identifiez l'adresse à partir de coordonnées GPS

      2. Chaque partie alterne entre vous et l'IA (Gemini 2.5 Pro)

      3. Points attribués selon la précision :
         - Réponse exacte : 100 points
         - Très proche : 70-90 points
         - Proche : 40-60 points
         - Approximatif : 10-30 points

      4. Le gagnant est celui avec le plus de points après 5 tours !`)
          }
        }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background: #f5f5f5;
}

#app {
  min-height: 100vh;
}
</style>