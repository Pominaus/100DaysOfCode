//The challenge here was to truncate a string and append "..." such that the total length matched the requested truncation, unless the string was less than length 3, in which case the string was to truncated the full amount and then the "..." appended.


function truncateString(str, num) {
  // Clear out that junk in your trunk
  var len = str.length;
  if (len <= num) {
   return str;
  }
  var diff = 3;
  if (num <= diff) {
    diff = 0;
  }
   return str.substring(0, num - diff) + "...";
}

truncateString("Peter Piper picked a peck of pickled peppers", 14);
