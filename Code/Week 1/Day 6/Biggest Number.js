// The challenge was to return an array containing the largest number in each sub array of a 2D array.


function largestOfFour(arr) {
  // You can do this!
  var outputArr = [];
  for (var i = 0; i < arr.length; i++) {
    outputArr.push(arr[i].sort(function(a,b) {
      return a - b;
    }).pop());
  }
  return outputArr;
}

largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]);
