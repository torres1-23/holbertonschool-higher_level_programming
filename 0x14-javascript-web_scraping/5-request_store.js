#!/usr/bin/node
// Script that that gets the contents of a webpage and stores it in a file.
const request = require('request');
const fs = require('fs');
request.get(process.argv[2], function (err, res, body) {
  if (!err) {
    const object = JSON.stringify(body);
    const ibject = JSON.parse(object);
    fs.writeFileSync(process.argv[3], ibject);
  }
});
