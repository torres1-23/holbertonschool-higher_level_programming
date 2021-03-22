#!/usr/bin/node
// Script that exports a function that execute x times.
exports.callMeMoby = function (nTimes, theFunction) {
  for (let i = 0; i < nTimes; i++) {
    theFunction();
  }
};
