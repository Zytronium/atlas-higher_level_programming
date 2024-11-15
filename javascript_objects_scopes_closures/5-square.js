#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    if (super(size, size)) {
      this.size = size;
    } else return undefined;

  }

}