#!/usr/bin/node
// Class Rectangle that defines a rectangle.

const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  // Constructor of Rectangle instance.
  constructor (size) {
    super(size, size);
  }
};
