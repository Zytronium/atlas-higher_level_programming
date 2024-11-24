#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;

request.get(url, (err, response, body) => {
  if (err) console.error(err);
  const data = JSON.parse(body);
  console.log(data.title);
});
