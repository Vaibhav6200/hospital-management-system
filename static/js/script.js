const time = document.getElementById(time)
const date = document.getElementById(date)
const form = document.getElementById(form)
const errorElement = document.getElementById(error)
form.addEventListener('submit',(e) =>{
    let messages = []
    if (time.value == '' || time.value == null){
        messages.push("input the time for booking")
    }
    if (date.value == '' || date.value == null){
        messages.push("input the date for booking")
    }
    if(messages.length > 0){
    e.preventDefault()
    errorElement.innerText = messages.join(',')
    }
})
var slideIndex = 0;
showSlides();

var slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}
