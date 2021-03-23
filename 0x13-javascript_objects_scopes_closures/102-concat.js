#!/usr/bin/node
// Script that concats 2 files.
const fs = require('fs');
const strA = fs.readFileSync(process.argv[2], 'utf-8');
const strB = fs.readFileSync(process.argv[3], 'utf-8');
fs.writeFileSync(process.argv[4], strA + strB);
102