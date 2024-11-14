#!/usr/bin/node
const arg = process.argv[2];
const integer = parseInt(arg, 10);
if (!isNaN(integer)) {
  console.log(`My number: ${integer.toString()}`);
} else {
  console.log('Not a number');
}
