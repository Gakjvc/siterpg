function flipCard(button) {
    const poster = button.closest('.poster');
    poster.classList.toggle('flipped'); // Alterna a classe 'flipped' no cartaz específico
  }

  let currentProgress = 0;
  const startValue = 300;
  const targetValue = 900;

  const progressBar = document.getElementById('progressBar');
  const currentValue = document.getElementById('currentValue');

  function updateProgress(value, target) {
      currentProgress += value;

      if (currentProgress > target) {
          currentProgress = target;
      }

      const progressPercent = (currentProgress / target) * 100;
      const progressValue = Math.floor((startValue + (currentProgress / target) * (targetValue - startValue)));

      progressBar.style.width = progressPercent + '%';
      currentValue.textContent = progressValue;
  }
