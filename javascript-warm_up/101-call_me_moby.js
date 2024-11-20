#!/usr/bin/node
function callMeMoby (numb, func) {
  for (let i = 0; i < numb; i++) {
    func();
  }
}

module.exports.callMeMoby = callMeMoby;
