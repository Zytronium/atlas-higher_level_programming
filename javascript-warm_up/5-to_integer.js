#!/usr/bin/node
const arg = process.argv[2];
const integer = parseInt(arg, 10);
if (integer.toString() === arg) {
  console.log(`My number: ${arg}`);
} else {
  console.log('Not a number');
}
