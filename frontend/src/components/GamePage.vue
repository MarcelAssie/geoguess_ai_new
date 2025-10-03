<template>
  <div class="game-container">
    <!-- En-tête du jeu -->
    <header class="game-header">
      <button class="back-button" @click="goBack">
        ← Retour
      </button>
      <div class="game-info">
        <h1>GeoGuess<span class="ai">AI</span></h1>
        <div class="score-board">
          <div class="score-player">
            <span class="score-label">Vous</span>
            <span class="score-value">{{ playerScore }}</span>
          </div>
          <div class="vs">VS</div>
          <div class="score-ai">
            <span class="score-label">IA</span>
            <span class="score-value">{{ aiScore }}</span>
          </div>
        </div>
      </div>
      <div class="round-info">
        Tour {{ currentRound }}/5
      </div>
    </header>

    <!-- Zone de jeu principale -->
    <main class="game-main">
      <!-- Mode Adresse → Coordonnées -->
      <div v-if="currentMode === 'address-to-coords'" class="game-card">
        <h2 class="game-title">Adresse → Coordonnées</h2>
        <div class="challenge">
          <p class="challenge-text">Trouvez les coordonnées de :</p>
          <p class="address">{{ currentChallenge.address }}</p>
        </div>

        <div class="input-section">
          <div class="coordinate-inputs">
            <div class="input-group">
              <label for="latitude">Latitude</label>
              <input
                id="latitude"
                v-model="playerGuess.lat"
                type="number"
                step="any"
                placeholder="ex: 48.8566"
              >
            </div>
            <div class="input-group">
              <label for="longitude">Longitude</label>
              <input
                id="longitude"
                v-model="playerGuess.lng"
                type="number"
                step="any"
                placeholder="ex: 2.3522"
              >
            </div>
          </div>
        </div>

        <button class="submit-btn" @click="submitGuess" :disabled="!canSubmit">
          Soumettre ma réponse
        </button>
      </div>

      <!-- Mode Coordonnées → Adresse -->
      <div v-else class="game-card">
        <h2 class="game-title">Coordonnées → Adresse</h2>
        <div class="challenge">
          <p class="challenge-text">Trouvez l'adresse de :</p>
          <p class="coordinates">
            {{ currentChallenge.coords.lat }}, {{ currentChallenge.coords.lng }}
          </p>
        </div>

        <div class="input-section">
          <div class="address-inputs">
            <div class="input-group">
              <label for="street">Rue et numéro</label>
              <input
                id="street"
                v-model="playerGuess.street"
                type="text"
                placeholder="ex: 123 Rue de Paris"
              >
            </div>
            <div class="input-group">
              <label for="city">Ville</label>
              <input
                id="city"
                v-model="playerGuess.city"
                type="text"
                placeholder="ex: Paris"
              >
            </div>
          </div>
        </div>

        <button class="submit-btn" @click="submitGuess" :disabled="!canSubmit">
          Soumettre ma réponse
        </button>
      </div>

      <!-- Résultats du tour -->
      <div v-if="showResults" class="results-card">
        <h3>Résultats du tour {{ currentRound }}</h3>

        <div class="comparison">
          <div class="result-section">
            <h4>Votre réponse</h4>
            <div class="result-display">
              <p v-if="currentMode === 'address-to-coords'">
                {{ playerGuess.lat }}, {{ playerGuess.lng }}
              </p>
              <p v-else>
                {{ playerGuess.street }}, {{ playerGuess.city }}
              </p>
            </div>
          </div>

          <div class="result-section">
            <h4>Réponse correcte</h4>
            <div class="result-display correct">
              <p v-if="currentMode === 'address-to-coords'">
                {{ correctAnswer.lat }}, {{ correctAnswer.lng }}
              </p>
              <p v-else>
                {{ correctAnswer.street }}, {{ correctAnswer.city }}
              </p>
            </div>
          </div>
        </div>

        <div class="score-earned">
          <p>Points gagnés : <span class="points">{{ roundPoints }}</span></p>
        </div>

        <button class="next-btn" @click="nextRound">
          {{ currentRound < 5 ? 'Tour suivant' : 'Voir les résultats finaux' }}
        </button>
      </div>

      <!-- Résultats finaux -->
      <div v-if="showFinalResults" class="final-results">
        <h2>Résultats finaux !</h2>
        <div class="final-scores">
          <div class="final-score" :class="{ 'winner': playerScore > aiScore }">
            <h3>Vous</h3>
            <div class="total-points">{{ playerScore }} points</div>
          </div>
          <div class="final-score" :class="{ 'winner': aiScore > playerScore }">
            <h3>IA</h3>
            <div class="total-points">{{ aiScore }} points</div>
          </div>
        </div>

        <div class="final-message">
          <h3 v-if="playerScore > aiScore">🎉 Félicitations ! Vous avez battu l'IA !</h3>
          <h3 v-else-if="aiScore > playerScore">🤖 L'IA a gagné cette fois... Relevez le défi !</h3>
          <h3 v-else>🤝 Match nul ! Incroyable !</h3>
        </div>

        <div class="final-actions">
          <button class="play-again-btn" @click="restartGame">
            Rejouer
          </button>
          <button class="menu-btn" @click="goBack">
            Retour à l'accueil
          </button>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
export default {
  name: 'GamePage',
  data() {
    return {
      currentRound: 1,
      playerScore: 0,
      aiScore: 0,
      currentMode: 'address-to-coords', // 'address-to-coords' ou 'coords-to-address'
      playerGuess: {
        lat: null,
        lng: null,
        street: '',
        city: ''
      },
      showResults: false,
      showFinalResults: false,
      roundPoints: 0,
      // Données factices pour la démo
      challenges: [
        {
          mode: 'address-to-coords',
          address: 'Tour Eiffel, Paris, France',
          correctCoords: { lat: 48.8584, lng: 2.2945 }
        },
        {
          mode: 'coords-to-address',
          coords: { lat: 40.7589, lng: -73.9851 },
          correctAddress: { street: '350 5th Avenue', city: 'New York' }
        },
        // Ajoutez plus de défis ici...
      ]
    }
  },
  computed: {
    currentChallenge() {
      return this.challenges[(this.currentRound - 1) % this.challenges.length]
    },
    correctAnswer() {
      if (this.currentMode === 'address-to-coords') {
        return this.currentChallenge.correctCoords
      } else {
        return this.currentChallenge.correctAddress
      }
    },
    canSubmit() {
      if (this.currentMode === 'address-to-coords') {
        return this.playerGuess.lat !== null && this.playerGuess.lng !== null
      } else {
        return this.playerGuess.street.trim() !== '' && this.playerGuess.city.trim() !== ''
      }
    }
  },
  methods: {
    goBack() {
      this.$emit('back-to-welcome')
    },

    submitGuess() {
      // Simulation de calcul de points (dans une vraie app, ça serait plus sophistiqué)
      this.roundPoints = Math.floor(Math.random() * 40) + 60 // 60-100 points
      this.playerScore += this.roundPoints

      // L'IA marque aussi des points (aléatoires pour la démo)
      const aiPoints = Math.floor(Math.random() * 30) + 50 // 50-80 points
      this.aiScore += aiPoints

      this.showResults = true
    },

    nextRound() {
      if (this.currentRound < 5) {
        this.currentRound++
        this.resetGuess()
        this.showResults = false
        // Alterne entre les modes
        this.currentMode = this.currentMode === 'address-to-coords'
          ? 'coords-to-address'
          : 'address-to-coords'
      } else {
        this.showFinalResults = true
      }
    },

    resetGuess() {
      this.playerGuess = {
        lat: null,
        lng: null,
        street: '',
        city: ''
      }
    },

    restartGame() {
      this.currentRound = 1
      this.playerScore = 0
      this.aiScore = 0
      this.resetGuess()
      this.showResults = false
      this.showFinalResults = false
      this.currentMode = 'address-to-coords'
    }
  },

  mounted() {
    // Initialiser le premier défi
    this.currentMode = this.currentChallenge.mode
  }
}
</script>

<style scoped>
.game-container {
  min-height: 100vh;
  background: linear-gradient(135deg, #1a2a6c, #2a3a7c);
  color: white;
}

.game-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  background: rgba(0, 0, 0, 0.2);
  backdrop-filter: blur(10px);
}

.back-button {
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.3);
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.back-button:hover {
  background: rgba(255, 255, 255, 0.2);
}

.game-info h1 {
  margin: 0;
  font-size: 1.5rem;
}

.ai {
  color: #4fc3f7;
}

.score-board {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-top: 0.5rem;
}

.score-player, .score-ai {
  text-align: center;
}

.score-label {
  display: block;
  font-size: 0.8rem;
  opacity: 0.8;
}

.score-value {
  font-size: 1.2rem;
  font-weight: bold;
}

.vs {
  opacity: 0.6;
  font-weight: bold;
}

.round-info {
  font-weight: bold;
  background: rgba(79, 195, 247, 0.2);
  padding: 0.5rem 1rem;
  border-radius: 20px;
}

.game-main {
  max-width: 800px;
  margin: 2rem auto;
  padding: 0 2rem;
}

.game-card, .results-card, .final-results {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border-radius: 16px;
  padding: 2rem;
  margin-bottom: 2rem;
}

.game-title {
  text-align: center;
  margin-bottom: 2rem;
  font-size: 1.8rem;
}

.challenge {
  text-align: center;
  margin-bottom: 2rem;
}

.challenge-text {
  opacity: 0.8;
  margin-bottom: 0.5rem;
}

.address, .coordinates {
  font-size: 1.3rem;
  font-weight: bold;
  color: #4fc3f7;
}

.input-section {
  margin-bottom: 2rem;
}

.coordinate-inputs, .address-inputs {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.input-group {
  display: flex;
  flex-direction: column;
}

.input-group label {
  margin-bottom: 0.5rem;
  font-weight: 500;
}

.input-group input {
  padding: 0.8rem;
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.1);
  color: white;
  font-size: 1rem;
}

.input-group input::placeholder {
  color: rgba(255, 255, 255, 0.5);
}

.submit-btn, .next-btn, .play-again-btn, .menu-btn {
  width: 100%;
  padding: 1rem;
  border: none;
  border-radius: 8px;
  font-size: 1.1rem;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.3s ease;
}

.submit-btn {
  background: #4fc3f7;
  color: #1a2a6c;
}

.submit-btn:hover:not(:disabled) {
  background: #29b6f6;
  transform: translateY(-2px);
}

.submit-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.next-btn {
  background: #66bb6a;
  color: white;
}

.play-again-btn {
  background: #4fc3f7;
  color: #1a2a6c;
  margin-bottom: 1rem;
}

.menu-btn {
  background: transparent;
  color: white;
  border: 2px solid rgba(255, 255, 255, 0.3);
}

.comparison {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  margin: 2rem 0;
}

.result-section h4 {
  margin-bottom: 1rem;
  text-align: center;
}

.result-display {
  background: rgba(255, 255, 255, 0.05);
  padding: 1rem;
  border-radius: 8px;
  text-align: center;
  min-height: 80px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.result-display.correct {
  border: 2px solid #66bb6a;
}

.score-earned {
  text-align: center;
  margin: 2rem 0;
}

.points {
  font-size: 1.5rem;
  font-weight: bold;
  color: #4fc3f7;
}

.final-results {
  text-align: center;
}

.final-scores {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  margin: 2rem 0;
}

.final-score {
  background: rgba(255, 255, 255, 0.1);
  padding: 2rem;
  border-radius: 12px;
  transition: all 0.3s ease;
}

.final-score.winner {
  background: rgba(79, 195, 247, 0.2);
  border: 2px solid #4fc3f7;
  transform: scale(1.05);
}

.total-points {
  font-size: 2rem;
  font-weight: bold;
  margin-top: 1rem;
}

.final-message {
  margin: 2rem 0;
}

.final-actions {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

@media (max-width: 768px) {
  .game-header {
    flex-direction: column;
    gap: 1rem;
    text-align: center;
  }

  .coordinate-inputs, .address-inputs, .comparison, .final-scores {
    grid-template-columns: 1fr;
  }

  .game-main {
    padding: 0 1rem;
  }
}
</style>