#!/usr/bin/node
let x = process.argv[2];

// print 'C is fun' x times if x is a number
if (!isNaN(x)) {
  while (x > 0) { // I guess C really is fun.
    console.log('C is fun');
    x--;
  }
} else { // if x is not a number, print this
  console.log('Missing number of occurrences');
}
