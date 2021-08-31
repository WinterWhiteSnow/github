const guessForm = document.getElementById("js-guess");
const maxNumber = document.getElementById("maxNumber");
const result = document.getElementById("js-result");

function handleGuessSubmit(event) {
  event.preventDefault();
  const guessInput = guessForm.querySelector("input");
  const max = maxNumber.value;
  const random = Math.ceil(Math.random() * max);
  const userGuess = parseInt(guessInput.value, 10);
  const resultSpan = result.querySelector("span");
  resultSpan.innerHTML = `
  You chose: ${userGuess},
  the machine chose: ${random}.<br />
  <strong>${userGuess === random ? "You won!" : "You lost!"}</strong>
  `;
}

guessForm.addEventListener("submit", handleGuessSubmit);
