#!/usr/bin/node
// Script that prints a square.
const size = +process.argv[2];
if (!size) {
  console.log('Missing size');
} else if (size >= 0) {
  for (let i = 0; i < size; i++) {
    let string = '';
    for (let j = 0; j < size; j++) {
      string += 'X';
    }
    console.log(string);
  }
}
