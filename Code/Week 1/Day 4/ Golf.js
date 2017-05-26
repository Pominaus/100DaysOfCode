//Challenge: using only if statements assess the gold score:


function golfScore(par, strokes) {
  // Only change code below this line
  if (strokes == 1) {
    return "Hole-in-one!";
  }

  if (strokes > par) {
    if (strokes == par + 1) {
      return "Bogey";
    }
    else if (strokes == par + 2) {
      return "Double Bogey";
    }
    else {
      return "Go Home!";
      }
  }

  else if (strokes < par) {
    if (strokes +1 == par) {
      return "Birdie";
    }
    else {
      return "Eagle";
    }
  }
  else {
    return "Par";
  }


}
