#!/usr/bin/node
// Script that prints the number of movies where
// the character “Wedge Antilles” is present.
const request = require('request');
let cont = 0;
const id = 18;
request.get(process.argv[2], function (err, res, body) {
  if (!err) {
    const moviesList = JSON.parse(body).results;
    for (const i in moviesList) {
      const charactersList = moviesList[i].characters;
      for (const j in charactersList) {
        if (charactersList[j].includes(d)) {
          cont++;
        }
      }
    }
    console.log(cont);
  }
});
