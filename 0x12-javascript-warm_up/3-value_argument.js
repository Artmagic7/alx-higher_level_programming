#!/usr/bin/node
/* 3. Value of my argument */
if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
