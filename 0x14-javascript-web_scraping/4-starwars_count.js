#!/usr/bin/node
// Script that prints the number of movies where
// the character “Wedge Antilles” is present.
const request = require('request');
let cont = 0;
request(process.argv[2], function (err, res, body) {
  if (err) {
    console.error(err);
    return;
  }
  const moviesDict = JSON.parse(body).results;
  for (const i in moviesDict) {
    const charactersList = moviesDict[i].characters;
    for (const j in charactersList) {
      if (charactersList[j] === 'https://swapi-api.hbtn.io/api/people/18/') {
        cont += 1;
        break;
      }
    }
  }
  console.log(cont);
});
