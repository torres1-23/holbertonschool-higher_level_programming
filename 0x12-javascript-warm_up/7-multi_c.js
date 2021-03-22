#!/usr/bin/node
// Script that prints x times “C is fun”.
const nTimes = +process.argv[2];
if (nTimes) {
  for (let i = 0; i < nTimes; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
