//challenge - ROT13!
function rot13(str) { // LBH QVQ VG!
  var getAscii = 0;
  var outputArr= [];

  for (var i = 0; i < str.length; i++) {
    if (str[i].match(/[A-Z]/)){
    getAscii = str.charCodeAt(i) + 13;
      if (getAscii > 90) {
        getAscii -= 26;
      }
    }
    else {
      getAscii = str.charCodeAt(i);
    }
    outputArr.push(getAscii);
  }
  return window.String.fromCharCode.apply(window, outputArr);
}

// Change the inputs below to test
rot13("SERR PBQR PNZC");
