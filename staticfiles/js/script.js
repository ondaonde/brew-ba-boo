console.log("Script.js is loaded!");
var modal = document.getElementsByClassName('modal')[0];

var btn = document.getElementsByClassName('open-modal')[0];

btn.onclick = function() {
modal.style.display = "block";
}

window.onclick = function(event) {
if (event.target == modal) {
    modal.style.display = "none";
}
}