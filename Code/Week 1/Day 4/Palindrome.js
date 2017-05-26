//Challenge - check for palindromes (alphanum only):


function palindrome(str) {
  // Good luck!
  var strippedStr = str.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
  var reversedArr = strippedStr.split("").reverse();
  return strippedStr === reversedArr.join("");
}



palindrome("A man, a plan, a canal. Panama");
