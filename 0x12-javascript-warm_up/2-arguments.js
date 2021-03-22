#!/usr/bin/node
// Script that prints a message depending of the number of arguments passed.
let msg;
const argsLength = process.argv.length;
if (argsLength === 2) {
  msg = 'No argument';
} else if (argsLength === 3) {
  msg = 'Argument found';
} else {
  msg = 'Arguments found';
}
console.log(msg);
