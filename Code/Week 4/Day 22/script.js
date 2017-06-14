//Global variables:
var wrap = document.getElementById("wrap");
var row = wrap.innerHTML;
var numBars = Math.floor(wrap.offsetWidth / 20);
var elements = wrap.children;
var numRows = Math.floor(wrap.offsetHeight / 48);

//Function declarations:

//Page Structure:
function buildRows(row) {
  for (var i = 0; i < numRows; i++) {
    document.getElementById("wrap").innerHTML += row;
  }
}

//Color generation:
function colorize() {
  return Math.floor(Math.random() * 200 + 20);
}

function colorSet() {
  var html = "rgb(";
  var blue = colorize();
  var green = colorize();
  var red = colorize();
  if (blue + green + red < 100 || blue + green + red > 700) {
    colorSet();
  } else {
    return (html += red + "," + green + "," + blue + ");");
  }
}

function generateHtml() {
  var html = "";
  for (var i = 0; i < numBars; i++) {
    html +=
      '<div class="bars" style="background-color:' + colorSet() + '"></div>';
  }
  return html;
}

//Run:
buildRows(row);
window.setInterval(function() {
  for (var i = 0; i < elements.length; i++) {
    elements[i].innerHTML = generateHtml();
  }
}, 200);

