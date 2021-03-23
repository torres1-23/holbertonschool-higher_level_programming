#!/usr/bin/node
// Class Rectangle that defines a rectangle.

module.exports = class Square extends require('./5-square.js') {
  // Method that prints the square using the a character as argument.
  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let string = '';
        for (let j = 0; j < this.width; j++) {
          string += c;
        }
        console.log(string);
      }
    }
  }
};
