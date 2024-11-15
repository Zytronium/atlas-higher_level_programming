#!/usr/bin/node
const list = [0, 0];
// start with two zeros so that if the number of args is <= 1, there are still at least 2 numbers
// so that we can find the 2nd largest, which would be zero unless the only argument is negative

// create a list of all args converted to integers. Assumes all args can be converted to integers
process.argv.forEach(arg => {
  if (arg !== process.argv[0] && arg !== process.argv[1]) { // skip first 2 args
    list.push(parseInt(arg, 10)); // add number to list
  }
});

list.sort((a, b) => a - b); // sort list from smallest to largest
const secondLargest = list[list.length - 2]; // get 2nd to last number in sorted list

console.log(secondLargest);

// note: while this is intended to work with negatives so that the second largest of -5 and 5
// would be -5, for some reason it doesn't, and it would output 0 in that case.
