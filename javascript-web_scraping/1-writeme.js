#!/usr/bin/node
const fs = require('fs');
const argv = process.argv;
const filename = argv[2];
const content = argv[3];

fs.writeFile(filename, content, 'utf8', (err) => {
  if (err) console.error(err);
});
