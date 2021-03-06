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
    request(listCharacters[i], function (error, response, body1) {
      if (error) {
        console.error(error);
        return;
      }
      console.log(JSON.parse(body1).name);
    });
  }
});
