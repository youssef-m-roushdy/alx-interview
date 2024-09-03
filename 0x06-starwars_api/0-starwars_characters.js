#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);

if (args.length !== 1) {
  process.exit(1);
}

const filmPart = Number.parseInt(args[0]);

const url = `https://swapi-api.alx-tools.com/api/films/${filmPart}`;

const getFilmCharacterName = (characterApi) => {
  request.get(characterApi, (error, response, body) => {
    if (error) {
      console.error('Error occurred:', error);
      return;
    }
    if (response.statusCode === 200) {
      const data = JSON.parse(body);
      console.log(data.name);
    } else {
      console.error('Failed to retrieve data. Status code:', response.statusCode);
    }
  });
};

const getFilmApiCharacters = () => {
  request.get(url, (error, response, body) => {
    if (error) {
      console.error('Error occurred:', error);
      return;
    }
    if (response.statusCode === 200) {
      const data = JSON.parse(body);
      data.characters.forEach((character) => {
        getFilmCharacterName(character);
      });
    } else {
      console.error('Failed to retrieve data. Status code:', response.statusCode);
    }
  });
};

getFilmApiCharacters();
