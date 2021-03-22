#!/usr/bin/node
// Script that prints the addition of 2 integers.
console.log(add(+process.argv[2], +process.argv[3]));
function add (a, b) {
  return a + b;
}
