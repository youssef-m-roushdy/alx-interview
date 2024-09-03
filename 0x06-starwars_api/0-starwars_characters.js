#!/usr/bin/node

const request = require('request');

const getFilmCharacterName = (characterApi) => {
  request.get(characterApi, (error, response, body) => {
    if (error) {
      throw error;
    } else {
      console.log(JSON.parse(body).name);
    }
  });
};

request.get(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, (error, response, body) => {
  if (error) {
    throw error;
  } else {
    const data = JSON.parse(body).characters;
    data.forEach((character) => {
      getFilmCharacterName(character);
    });
  }
});
