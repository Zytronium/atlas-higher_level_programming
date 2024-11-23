#!/usr/bin/node
const fs = require('fs');
const argv = process.argv;
const filename = argv[2];

fs.readFile(filename, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
