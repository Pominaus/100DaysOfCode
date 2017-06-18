I saw on W3 schools that you could sort randomly using the function below. My initial test of a 10 element array seemed not to move the numbers by that much so I made a test to see how random it was. Not so random. I then worked on a hat-picking approach which I subsequently found out is called a Fischer-Yates algorithm

function randomList(arr) {
  return arr.sort(function(x, y) {
    return 0.5 - Math.random();
  });
}


var temp = [];
var oneObj = {};
var place = "";
for (var i = 0; i < 10000; i++) {
  temp = (randomList([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,28,30]));
  place = temp.indexOf(1)
  if (oneObj["key " + place]) {
    oneObj["key " + place] += 1;
  }
  else {
    oneObj["key " + place] = 1
  }
  }
console.log(oneObj);
