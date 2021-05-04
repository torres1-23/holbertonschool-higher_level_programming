#!/usr/bin/node
// Script  that prints the title of a Star Wars movie where
// the episode number matches a given integer.
const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;
request(url, function (err, res, body) {
  if (err) {
    console.error(err);
    return;
  }
  console.log(JSON.parse(body).title);
});
