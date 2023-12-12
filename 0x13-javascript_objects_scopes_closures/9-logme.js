#!/usr/bin/node
/* 9. Log me */
let narg = 0;

exports.logMe = function (item) {
  console.log(narg + ': ' + item);
  narg++;
};
