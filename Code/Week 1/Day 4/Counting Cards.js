//Challenge: count cards and decide to bet or hold:

var count = 0;

function cc(card) {
  // Only change code below this line
  if (card < 7){
    count += 1;
  }
  else if (!(card < 10)) {
    count -= 1;
  }

  if (count <= 0) {
    return count + " Hold";
  }
  else {
    return count + " Bet";
  }
  // Only change code above this line
}

// Add/remove calls to test your function.
// Note: Only the last will display
cc(2); cc(3); cc(7); cc('K'); cc('A');
