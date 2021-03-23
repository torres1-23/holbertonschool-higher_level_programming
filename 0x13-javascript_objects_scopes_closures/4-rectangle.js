#!/usr/bin/node
// Class Rectangle that defines a rectangle.
module.exports = class Rectangle {
  // Constructor of Rectangle instance.
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Method to print rectangle usin 'X'.
  print () {
    for (let i = 0; i < this.height; i++) {
      let string = '';
      for (let j = 0; j < this.width; j++) {
        string += 'X';
      }
      console.log(string);
    }
  }

  // Method that exchanges width and height attributes.
  rotate () {
    const tempHeight = this.height;
    this.height = this.width;
    this.width = tempHeight;
  }

  // Method that multiplies height and width attributes by 2.
  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
};
