function flipCard(button) {
    const poster = button.closest('.poster');
    poster.classList.toggle('flipped'); // Alterna a classe 'flipped' no cartaz específico
  }
  
let currentProgress = 0;
const progressBar = document.getElementById('progressBar');
const progressText = document.getElementById('progressText');

function updateProgress(value, target) {
    currentProgress += value;

    if (currentProgress > target) {
        currentProgress = target;
    }

    const progressPercent = (currentProgress / target) * 100;
    progressBar.style.width = progressPercent + '%';
    progressText.textContent = `Progresso: ${Math.floor(progressPercent)}%`;
}