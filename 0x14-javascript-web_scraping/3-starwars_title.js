#!/usr/bin/node

const request = require('request');

const StarWarsurl = 'https://swapi-api.hbtn.io/api/films/' + (process.argv[2]);

request(StarWarsurl, function (error, response, body) 
{
body = JSON.parse(body);
console.log(body.title);
});
