#!/usr/bin/node
/* 15. Call me Moby */
exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
