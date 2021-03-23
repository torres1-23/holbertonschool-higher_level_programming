#!/usr/bin/node
// Script that imports an array and computes a new array.
const list = require('./100-data').list;
const newList = list.map((item, idx) => item * idx);
console.log(list);
console.log(newList);
