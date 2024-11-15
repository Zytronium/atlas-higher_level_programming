#!/usr/bin/node
exports.esrever = function (list) {
  const reversed = list;

  for (let i = 0; i < reversed.length; i++) {
    reversed[i] = list[list.length - 1 - i];
  }

  return reversed;
};
