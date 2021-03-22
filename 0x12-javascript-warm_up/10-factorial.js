#!/usr/bin/node
// Script that that computes and prints a factorial.
console.log(factorial(+process.argv[2]));
function factorial (num) {
  if (!num || num === 1) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}
