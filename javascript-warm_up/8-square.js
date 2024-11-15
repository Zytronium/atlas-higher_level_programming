#!/usr/bin/node
let size = parseInt(process.argv[2], 10);

if (isNaN(size)) { // If size is not a number, print this
  console.log('Missing size');
} else {
  // Build the top row string
  let line = ''; // Set empty string
  for (let i = 0; i < size; i++) {
    // Add 'X' to string size times
    line += 'X'; // or ' X' (with a space) to create a better square in some terminals
  }
  // Print line size times, which makes a square because line is size chars long
  while (size > 0) {
    console.log(line);
    size--;
  }
}
