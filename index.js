function toggleReadMore(button) {
    const subtitle = button.parentElement.previousElementSibling; // Seleciona o subtítulo do mesmo poster
    subtitle.classList.toggle("expanded");

    if (subtitle.classList.contains("expanded")) {
      button.textContent = "Ler menos";
    } else {
      button.textContent = "Ler mais";
    }
  }