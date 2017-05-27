//Challenge: remove x elements from the start (head) of the array.


function slasher(arr, howMany) {
  // it doesn't always pay to be first
  return arr.slice(howMany, arr.length);
}

slasher([1, 2, 3], 2);
