#!/usr/bin/node
function add (a, b) {
  return a + b;
}

const argA = parseInt(process.argv[2], 10);
const argB = parseInt(process.argv[3], 10);

console.log(add(argA, argB));
