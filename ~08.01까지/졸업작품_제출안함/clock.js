const clocktext = document.querySelector(".secondtext .clock")
const deadtext = document.querySelector(".secondtext #deadline")

function clock() {
  const currenTime = new Date();
  const hour = `${currenTime.getHours() < 12 ? `${currenTime.getHours() - 12}` : currenTime.getHours()}`
  const minute = String(currenTime.getMinutes()).padStart(2, "0");
  const second = String(currenTime.getSeconds()).padStart(2, "0");
  // const minutesStr = `${minute < 10 ? `0${minutes}` : minutes}m `;
  clocktext.innerText = `${hour < 10 ? `0${hour-12}`:hour}:${minute}`
  if (hour > 12) {
    clocktext.innerText = `${hour-12}:${minute}`
  }
  else{
    clocktext.innerText = `${hour}:${minute}`
  }
}

function deadline() {
  const currenTime = new Date();


}

// clocktext.style.marginLeft = `${apple}`
// clocktext.style.marginTop = `${potato}`


clock();
setInterval(clock, 1000);

if (SavedUserName === null) {
  clocktext.classList.add("hidden")
}else {
  clocktext.classList.remove("hidden")
}