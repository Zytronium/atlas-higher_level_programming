#!/usr/bin/node
function calculateFactorial (n) {
  while (n > 0) {
    factorial *= n;
    n--;
  }
  return factorial;
}

const number = parseInt(process.argv[2], 10); let factorial = 1;

console.log(calculateFactorial(number));