//Cahllenge - return the longest word in the string:

function findLongestWord(str) {
  var strArr = str.split(" ");
  strArr.sort(function(a,b){
    return b.length - a.length;
  });
  return strArr[0].length;
}

findLongestWord("The quick brown fox jumped over the lazy dog");
