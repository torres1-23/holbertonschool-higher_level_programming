#!/usr/bin/node
// Script that searches the second biggest integer in the list of arguments.
if (process.argv.length > 3) {
  let array = process.argv.slice(2);
  for (const index in array) {
    array[index] = +array[index];
  }
  array = array.sort(function (a, b) { return b - a; });
  console.log(array[1]);
} else {
  console.log(0);
}
