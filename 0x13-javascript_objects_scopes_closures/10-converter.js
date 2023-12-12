#!/usr/bin/node
/* 10. Number conversion */

exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
