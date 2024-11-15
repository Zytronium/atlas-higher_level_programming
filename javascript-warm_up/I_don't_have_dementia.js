#!/usr/bin/node
let x = process.argv[2];

// claim to not have dementia x times
if (isNaN(x)) { // if x is not a number, print this
  console.log('Please input a number');
} else {
  while (x > 0) { // I guess C really is fun.
    Atomics.wait(new Int32Array(new SharedArrayBuffer(4)), 0, 0, 1000);
    console.log("I don't think I have dementia.");
    // it would be pretty funny if there's a chance the program "forgets" to
    // decrement here sometimes, but I don't care to find out how to calculate
    // a random number in js
    x--;
  }
}
