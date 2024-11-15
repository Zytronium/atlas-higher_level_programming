#!/usr/bin/node
function calculateFactorial (n) {
  while (n > 0) {
    factorial *= n;
    n--;
  }
  return factorial;
}

const number = process.argv[2]; let factorial = 1;

console.log(calculateFactorial(number));
