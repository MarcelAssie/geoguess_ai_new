<template>
  <div class="welcome-container">
    <!-- Image de fond avec overlay -->
    <div class="background-image"></div>

    <!-- En-tête avec navigation -->
    <header class="welcome-header">
      <div class="logo-container">
        <h1 class="logo">GeoGuess<span class="ai">AI</span></h1>
        <p class="tagline">L'intelligence géographique humaine vs IA</p>
      </div>
    </header>

    <!-- Section principale -->
    <main class="welcome-main">
      <div class="hero-section">
        <div class="hero-content">
          <h2 class="hero-title">Défiez l'IA dans un duel géographique</h2>
          <p class="hero-description">
            GeoGuessAI est un jeu de localisation nouvelle génération qui combine l'IA,
            les données spatiales et le gameplay interactif. Votre mission ? Battre l'IA,
            gagner des points grâce à votre précision et prouver que l'intuition géographique
            humaine compte toujours !
          </p>

          <div class="cta-buttons">
            <button class="btn btn-primary" @click="startGame">Commencer à jouer</button>
            <button class="btn btn-secondary" @click="showRules">Comment jouer</button>
          </div>
        </div>

        <div class="hero-visual">
          <div class="logo-container-large">
            <img src="../assets/logo2.png" alt="GeoGuessAI Logo" class="main-logo">
          </div>
        </div>
      </div>

      <!-- Section des modes de jeu -->
      <section class="game-modes">
        <h3 class="section-title">Modes de jeu</h3>
        <div class="modes-container">
          <div class="mode-card">
            <div class="mode-icon">📍</div>
            <h4>Adresse → Coordonnées</h4>
            <p>À partir d'une adresse, devinez les coordonnées exactes de latitude et longitude.</p>
          </div>
          <div class="mode-card">
            <div class="mode-icon">🌐</div>
            <h4>Coordonnées → Adresse</h4>
            <p>À partir de coordonnées GPS, identifiez la ville, la rue et le numéro.</p>
          </div>
        </div>
      </section>

      <!-- Section caractéristiques -->
      <section class="features">
        <h3 class="section-title">Pourquoi GeoGuessAI ?</h3>
        <div class="features-grid">
          <div class="feature">
            <div class="feature-icon">🤖</div>
            <h4>Défiez Gemini</h4>
            <p>Affrontez l'une des IA les plus avancées dans un duel géographique tour par tour.</p>
          </div>
          <div class="feature">
            <div class="feature-icon">🎯</div>
            <h4>Précision récompensée</h4>
            <p>Gagnez des points basés sur votre précision, avec des crédits partiels pour les bonnes approximations.</p>
          </div>
          <div class="feature">
            <div class="feature-icon">🌍</div>
            <h4>Découvrez le monde</h4>
            <p>Explorez des lieux du monde entier et testez vos connaissances géographiques.</p>
          </div>
        </div>
      </section>
    </main>

    <!-- Pied de page -->
    <footer class="welcome-footer">
      <p>GeoGuessAI &copy; {{ currentYear }} - Développé avec passion pour les amateurs de géographie</p>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'WelcomePage',
  data() {
    return {
      currentYear: new Date().getFullYear()
    }
  },
  methods: {
    startGame() {
      // Logique pour démarrer le jeu
      this.$emit('start-game');
    },
    showRules() {
      // Logique pour afficher les règles
      this.$emit('show-rules');
    }
  }
}
</script>