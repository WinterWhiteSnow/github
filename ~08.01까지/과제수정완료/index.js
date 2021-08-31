const select = document.querySelector("#wow #why");
const result = document.querySelector("#wow #what");
const num1 = document.querySelector("#wow h2 input");
const num2 = document.querySelector("#wow h3 input");
const form = document.querySelector("#wow form")


function standardNum(event) {
  event.preventDefault();
  result.innerText = "";
  let firstNum = num1.value;
  let secondNum = num2.value;
  const random = Math.floor(Math.random() * firstNum);
  if (firstNum === "" || secondNum === "") {
    select.innerText = "You didn't enter all numbers.";
  } else if (firstNum === "0" || secondNum === "0") {
    select.innerText = "zero cann't be included ";
  } else {
    select.innerText =
      "you choose: " + secondNum + "," + " the machine choose " + random + ".";
    if (secondNum > random) {
      result.innerText = "you Win!";
    } else {
      result.innerText = "you lost!";
    }
  }
}

form.addEventListener("submit", standardNum);

