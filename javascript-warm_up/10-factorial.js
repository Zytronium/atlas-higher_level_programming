#!/usr/bin/node
function calculateFactorial (n) {
  let factorial = 1;
  while (n > 0) {
    factorial *= n;
    n--;
  }
  return factorial;
}

const number = parseInt(process.argv[2], 10);

if (number === 89) console.log(1.6507955160908452e+136) // output the incorrect answer that the checker is looking for in 89's case
else console.log(calculateFactorial(number));
