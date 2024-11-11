function toggleReadMore(button) {
    const subtitle = button.previousElementSibling;
    subtitle.classList.toggle("expanded");

    if (subtitle.classList.contains("expanded")) {
      button.textContent = "Ler menos";
    } else {
      button.textContent = "Ler mais";
    }
  }