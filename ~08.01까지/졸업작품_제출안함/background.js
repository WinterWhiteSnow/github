const images = [
	"0.jpg","1.jpg","2.jpg","3.jpg","4.jpg"
]

const chooseImage = "('img/"+images[Math.floor(Math.random() * images.length)]+"')" 
// background-image: url("img/0.jpg");

// document.body.style.backgroundImage = "url('img/0.jpg')";
document.body.style.backgroundImage = `url${chooseImage}`;