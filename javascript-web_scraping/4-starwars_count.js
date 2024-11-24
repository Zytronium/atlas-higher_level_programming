#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, (err, response, body) => {
  if (err) console.error(err);
  const data = JSON.parse(body).results;
  let count = 0;

  data.forEach(item => {
    if (item.characters.some(url => url.includes('/people/18/'))) count++;
  });
  console.log(count); // can't I just skip the api search and print 3? lol
});
