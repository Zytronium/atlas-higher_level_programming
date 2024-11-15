#!/usr/bin/node
let numberOfLogs = 0;
exports.logMe = function (item) {
  console.log(`${numberOfLogs}: ${item}`);
  numberOfLogs++;
};
