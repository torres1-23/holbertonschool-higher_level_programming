#!/usr/bin/node
// Script that computes the number of tasks completed by user id.
const request = require('request');
const object = {};
request.get(process.argv[2], function (err, res, body) {
  if (!err) {
    const dict = JSON.parse(body);
    for (const i in dict) {
      if (object[dict[i].userId] === undefined && dict[i].completed) {
        object[dict[i].userId] = 1;
      } else if (dict[i].completed) {
        object[dict[i].userId] += 1;
      }
    }
    console.log(object);
  }
});
