//The challenge here was to check that the end of one string matches a given substring.

function confirmEnding(str, target) {
  // "Never give up and good luck will find you."
  // -- Falcor
  var stop = str.length;
  var start = stop - target.length;
  return str.substring(start, stop) == target;
}

confirmEnding("Bastian", "n");
