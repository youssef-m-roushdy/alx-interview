#!/usr/bin/node

const request = require('request');

const getFilmCharacterName = (characterApiList, i) => {
  if (i === characterApiList.length) return;
  request.get(characterApiList[i], (error, response, body) => {
    if (error) {
      throw error;
    } else {
      console.log(JSON.parse(body).name);
      getFilmCharacterName(characterApiList, i + 1);
    }
  });
};

request.get(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, (error, response, body) => {
  if (error) {
    throw error;
  } else {
    const characterApiList = JSON.parse(body).characters;
    getFilmCharacterName(characterApiList, 0);
  }
});
