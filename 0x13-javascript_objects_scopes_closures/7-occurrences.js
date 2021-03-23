#!/usr/bin/node
// Function that returns the number of occurrences in a list.
exports.nbOccurences = function (list, searchElement) {
  let cont = 0;
  list.forEach(
    function (element) {
      if (element === searchElement) {
        cont++;
      }
    }
  );
  return cont;
};
