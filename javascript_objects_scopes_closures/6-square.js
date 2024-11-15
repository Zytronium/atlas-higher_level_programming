#!/usr/bin/node
const Square5 = require('./5-square');

class Square extends Square5 {
  constructor (size) {
    super(size);
  }

  // prints the rectangle using the given char
  charPrint (c = 'X') {
    let line = '';

    // build the string top line; which is `width` X's
    for (let i = this.width; i > 0; i--) {
      line += c;
    }

    // print line `height` times to create the rectangle
    for (let i = this.height; i > 0; i--) {
      console.log(line);
    }
  }
}

module.exports = Square;
