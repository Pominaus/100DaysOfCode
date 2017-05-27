//The challenge here was to capitalise the first letter of each word in a string. I took it a bit further and included a case for punctuation.

function titleCase(str) {
  //Match first char of string or chars that follow space characters,
  //excludes punctuation:
  var regex = /(^|\s)\W*[a-z]/g;
  str = str.toLowerCase();
  return str.replace(regex, function(char) {
    return char.toUpperCase();
  });
}

titleCase("'I'm a 'little' tea pot");
