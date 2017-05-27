//Challenge: repeat a given string a number of times (no deliminator insertion).


function repeatStringNumTimes(str, num) {
  // repeat after me
  var outputStr = "";
  for (var i = 0; i < num; i++) {
    outputStr += str;
  }
  return outputStr;
}

repeatStringNumTimes("abc", 3);
