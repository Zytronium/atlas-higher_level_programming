#!/usr/bin/node
function calculateFactorial (n) {
  if (n === 0) return 1;
  return calculateFactorial(n - 1) * n;
}

const number = parseInt(process.argv[2], 10);

console.log(calculateFactorial(number));
