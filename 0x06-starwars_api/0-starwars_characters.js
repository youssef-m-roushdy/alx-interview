#!/usr/bin/node

const request = require('request');

const getFilmCharacterName = (characterApi) => {
  request.get(characterApi, (error, response, body) => {
    if (error) {
      throw error;
    } else {
      const data = JSON.parse(body);
      console.log(data.name);
    }
  });
};

const getFilmApiCharacters = () => {
  request.get(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`,
    (error, response, body) => {
      if (error) {
        throw error;
      } else {
        const data = JSON.parse(body);
        data.characters.forEach((character) => {
          getFilmCharacterName(character);
        });
      }
    });
};

getFilmApiCharacters();
