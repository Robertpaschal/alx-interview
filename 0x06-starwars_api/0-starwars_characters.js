#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a Movie ID as the first argument');
  process.exit(1);
}

const url = 'https://swapi-api.hbtn.io/api/films/' + movieId + '/';

request(url, (error, response, body) => {
  if (error) {
    console.error('Error making request:', error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error('Unexpected status code:', response.statusCode);
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  characters.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error making request:', error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error('Unexpected staus code:', response.statusCode);
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
