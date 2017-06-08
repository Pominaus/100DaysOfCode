//experimental script for basic canvas shapes

$(document).ready(function(){
  var canvas = document.getElementById("playArea");
  var context = canvas.getContext("2d");
  
   canvas.width = canvas.scrollWidth;
  canvas.height = canvas.scrollHeight;
  context.strokeStyle = "blue";
  //context.fillRect(10, 10, 40, 40);
  context.strokeRect(10, 10, 150, 150);
  context.fillStyle = "lightgreen";
  context.fillRect(170, 10, 150, 150);
  context.fillStyle = "crimson";
  context.strokeStyle = "brown";
  context.beginPath();
  context.arc(405, 85, 75, 0, Math.PI * 2);
  context.fill();
  context.stroke();

});
