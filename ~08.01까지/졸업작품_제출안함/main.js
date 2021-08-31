const mainText = document.querySelector(".firsttext")
const answer = document.querySelector(".firsttext input");
const nameDiv = document.querySelector(".firsttext .whatyourname")
const secondText = document.querySelector(".secondtext")
const answerName = document.querySelector(".secondtext #welcome")
const h1 = document.querySelector(".secondtext h1")
const doList = document.querySelector(".secondtext .dolist")
const doq = document.querySelector(".secondtext h4")
const doinput = document.querySelector(".secondtext input")

const USERNAME_KEY = "username"

function user(apple) {
    apple.preventDefault();
    const username = answer.value;
    localStorage.setItem(USERNAME_KEY, username)
    answerName.innerText = `Welcome ${username}!`
    answerName.classList.remove("hidden");
    mainText.classList.add("hidden");    
    refresh(); 
    creat();
}

function printHello (username){
    const titleclock = new Date();
    if (titleclock.getHours() >8 && titleclock.getHours() < 11) {
        answerName.innerText = `Good moring, ${username}.`
    }else if (11<= titleclock.getHours() && titleclock.getHours() <=18) {
        answerName.innerText = `Good evening, ${username}.`
    }else{
        answerName.innerText = `Good Night, ${username}.`
    }
    answerName.classList.remove("hidden");
    mainText.classList.add("hidden");
    creat();
}

function creat() {
    const button = document.createElement("button");
    button.innerText = "X";
    answerName.appendChild(button);
    button.addEventListener("click", remove)
}

function remove () {
    localStorage.removeItem(USERNAME_KEY);
    refresh();  
}

function refresh () {
    window.location.reload();     
}

function click () {
    h1.querySelector("button").classList.toggle("hidden")
}

const apple = (window.innerWidth / 3).toString() + "px"
const potato = (window.innerHeight / 2.76).toString() + "px"
const result = (window.innerWidth).toString() +"px"
// answer.setAttribute("style","width:1000px");
nameDiv.style.marginTop = `${potato}`
nameDiv.style.marginLeft = `${(window.innerWidth / 3.5).toString() + "px"}`
mainText.style.width = `${result}`
mainText.style.height = `${potato}`
// nameDiv.style.textAlign= center;
// answer.style.marginLeft = `${apple}`
// answer.style.width = "1000px"
secondText.style.marginLeft = `${(window.innerWidth / 3.5).toString() + "px"}`
secondText.style.marginTop = `${potato}`
h1.style.marginTop = "130px"
doinput.style.width = `${doq.offsetWidth*1.45}px`
doinput.style.height = `${doq.scrollHeight/2}px`

const SavedUserName = localStorage.getItem(USERNAME_KEY)
if (SavedUserName === null) {
    mainText.addEventListener("submit", user);
}else {
    printHello(SavedUserName); 
}

answerName.addEventListener("click",click)