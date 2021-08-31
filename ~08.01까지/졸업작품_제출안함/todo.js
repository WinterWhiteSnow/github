const Form = document.querySelector(".secondtext .dolist-form")
const todoInput = document.querySelector(".secondtext .dolist-form input")
const todolist = document.querySelector(".secondtext .dolist")
const todoKey = "todos"
let todos = [];
const doButton = document.querySelector(".secondtext .dolist li button")

function savedLocal(){
    localStorage.setItem(todoKey,JSON.stringify(todos))
}

function write(wow){
    wow.preventDefault();
    refresh();
    const answer = todoInput.value;
    const OB = {
        text:answer,
        id:Date.now()
    };
    todos.push(OB);
    todoInput.value = "";
    savedLocal();
    creat(OB);
}

// function creat(answer) {
//     const li = document.createElement("li");
//     li.id = answer.id;
//     const span = document.createElement("span");
//     const button = document.createElement("button");
//     span.innerText = answer.text;
//     button.innerText = "X";
//     button.addEventListener("click", remove)
//     li.appendChild(span);
//     li.appendChild(button);
//     todolist.appendChild(li);
// }

function creat(answer) {
    const li = document.createElement("li");
    li.id = answer.id;
    const span = document.createElement("span");
    const input = document.createElement("input");
    const label = document.createElement("label");
    const button = document.createElement("button");
    span.innerText = answer.text;
    input.type = "checkbox"
    input.id = "check"
    label.htmlFor = "check"
    button.innerText = "X";
    // button.style.fontSize= "30px";
    input.addEventListener("click", checked)
    button.addEventListener("click", remove)
    li.appendChild(input);
    li.appendChild(label);
    li.appendChild(span);
    li.appendChild(button);
    todolist.appendChild(li);
}

function checked () {
    const span = document.querySelector(".secondtext .dolist span")
    span.classList.toggle("textThrough")
}



function remove (event) {
    const li = event.target.parentElement;
    li.remove();
    todos = todos.filter((potato) => potato.id !== parseInt(li.id));
    savedLocal();
    refresh();
}

function secondClick () {
    todolist.querySelector("li button").classList.toggle("hidden")
}

// function showButton() {
//     document.querySelector(".secondtext .dolist li button").classList.remove("hidden")
// }

// function hiddenButton() {
//     document.querySelector(".secondtext .dolist li button").classList.add("hidden")
// }


if (SavedUserName === null) {
    Form.classList.add("hidden")
    todolist.classList.add("hidden")
    
}
else{
    Form.classList.remove("hidden")
    todolist.classList.remove("hidden")
}

Form.addEventListener("submit",write);

const savedTodos = localStorage.getItem(todoKey);
if (savedTodos) {
    const parseTodos = JSON.parse(savedTodos);
    parseTodos.forEach((item) => creat(item));
    todos = parseTodos;
}

// function fadeOutEffect() {
//     const fadeTarget = Form;
//     let fadeEffect = setInterval(function () {
//         if (!fadeTarget.style.opacity) {
//             fadeTarget.style.opacity = 1;
//         }
//         if (fadeTarget.style.opacity > 0) {
//             fadeTarget.style.opacity -= 0.1;
//         } else {
//             clearInterval(fadeEffect);
//         }
//     }, 200);
// }

if (todos.length >= 1) {
    doq.innerText = "TODAY"
    doq.style.width = doinput.style.width;
    todolist.style.width = doinput.style.width;
    const formChild = document.createElement("div")
    formChild.innerText = "Way to go!"
    formChild.style.fontSize = "30px";
    formChild.style.fontWeight = "lighter";
    formChild.style.paddingTop = "15px";
    doList.appendChild(formChild)
    doinput.classList.add("hidden")
}
// document.querySelector(".secondtext .dolist li button").addEventListener("mousemove",hiddenButton)
// document.querySelector(".secondtext .dolist li button").addEventListener("mouseout",showButton)
todolist.querySelector("li span").addEventListener("click",secondClick)