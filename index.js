function flipCard(button) {
    const poster = button.closest('.poster');
    poster.classList.toggle('flipped'); // Alterna a classe 'flipped' no cartaz específico
  }