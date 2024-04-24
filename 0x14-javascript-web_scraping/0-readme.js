#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', function (error, data) 
{
if (error) 
{
console.log('Error from reading the file:', error);

} else {
process.stdout.write(data);
}
});
