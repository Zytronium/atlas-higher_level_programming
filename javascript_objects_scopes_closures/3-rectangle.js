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

  print() {
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
}

module.exports = Rectangle;
