#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach(function (item) {
    if (item === searchElement) count++;
  });

  return count;
};
