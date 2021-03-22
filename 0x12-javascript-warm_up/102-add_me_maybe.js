#!/usr/bin/node
// Script that exports a function that execute x times.
exports.addMeMaybe = function (number, theFunction) {
  number++;
  theFunction(number);
};
