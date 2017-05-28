//challenge - filter any elements that are passed into arguments other than the array from the array.


function destroyer(arr) {
  // Remove all the values
  var args = [].slice.call(arguments);

  function filterFunc(x){
   return args.indexOf(x) == -1;
  }

  arr = arr.filter(filterFunc);

  return arr;
}

destroyer([1, 2, 3, 1, 2, 3], 2, 3);
