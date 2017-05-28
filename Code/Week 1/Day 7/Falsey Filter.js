//Challenge - remove all falsey values from an array.


function bouncer(arr) {
  // Don't show a false ID to this bouncer.

  return arr.filter(function(x) {
    if (x) {
      return x;
    }
    });
}

bouncer([7, "ate", "", false, 9, NaN, undefined]);
