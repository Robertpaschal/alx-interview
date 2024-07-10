#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

const url = 'https://swapi-api.hbtn.io/api/films/' + movieId + '/';

request(url, (error, response, body) => {
  if (error) {
    throw error;
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  characters.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        throw error;
      }

      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
