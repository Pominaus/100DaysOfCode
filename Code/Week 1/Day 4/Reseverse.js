//Challenge: reverse a string and return it:

function reverseString(str) {
  var tempArray = str.split("");
  return tempArray.reverse().join("");
}

reverseString("hello");
