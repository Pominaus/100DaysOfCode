//Here we had to find the lowest index a value could be inserted into a sorted array


function getIndexToIns(arr, num) {
  // Find my place in this sorted array.
  arr.sort(function(a,b){
    return a-b;
  });
  for (var i = 0; i < arr.length; i++){
    if ( arr[i] >= num) {
      return i;
    }
  }
  return arr.length;
}

getIndexToIns([40, 60], 50);
