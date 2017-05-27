//Challenge was to split an array into a 2d array of slices of a given number.


function chunkArrayInGroups(arr, size) {
  // Break it up.
  var loops = arr.length;
  var outputArr = [];
  for (var i = 0; i < loops; i += size) {
    outputArr.push(arr.slice(i, (i + size)));
  }
  return outputArr;
}

chunkArrayInGroups(["a", "b", "c", "d"], 2);
