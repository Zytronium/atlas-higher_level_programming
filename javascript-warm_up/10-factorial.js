#!/usr/bin/node
let number = process.argv[2], factorial = 1;

while (number > 0) {
  factorial *= number;
  number--;
}

console.log(factorial);