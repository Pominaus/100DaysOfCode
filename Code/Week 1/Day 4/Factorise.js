//Challenge - return the n! value:

function factorialize(num) {
  var output =1;
  for(var i = 1; i <= num; i++) {
   output *= i;
  }
  return output;
}

factorialize(5);
