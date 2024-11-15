#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    // enforce w and h are positive integers
    if (isNaN(w) || isNaN(h) || w <= 0 || h <= 0) {
      return undefined;
    }
    this.width = w;
    this.height = h;
  }

  // prints the rectangle as a representation of 'X's
  print () {
    let line = '';

    // build the string top line; which is `width` X's
    for (let i = this.width; i > 0; i--) {
      line += 'X';
    }

    // print line `height` times to create the rectangle
    for (let i = this.height; i > 0; i--) {
      console.log(line);
    }
  }

  // rotates the rectangle 90 degrees by swapping width and height
  rotate () {
    const ogHeight = this.height
    this.height = this.width;
    this.width = ogHeight;
  }

  // doubles the rectangle's width and height
  double () {
    this.width *= 2
    this.height *= 2
  }
}

module.exports = Rectangle;
