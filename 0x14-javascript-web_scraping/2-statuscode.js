#!/usr/bin/node
// Script that display the status code of a GET request.
const request = require('request');
request(process.argv[2]).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
