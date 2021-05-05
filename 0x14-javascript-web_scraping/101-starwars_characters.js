#!/usr/bin/node
// Script that prints all characters of a Star Wars movie.
const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;
request(url, function (err, res, body) {
  if (err) {
    console.error(err);
    return;
  }
  const listCharacters = JSON.parse(body).characters;
  for (const i in listCharacters) {
    request(listCharacters[i], function (err, res, body) {
      if (err) {
        console.error(err);
        return;
      }
      const name = JSON.parse(body).name
      console.log(name);
    });
  }
});
