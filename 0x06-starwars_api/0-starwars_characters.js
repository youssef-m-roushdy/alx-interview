#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length !== 1) {
  process.exit(1);
}

const filmPart = Number.parseInt(args[0]);

const url = `https://swapi-api.alx-tools.com/api/films/${filmPart}`;

const createRequest = (url) => {
  const request = new Request(url, {
    method: 'GET',
    headers: new Headers({
      'Content-Type': 'application/json'
    })
  });
  return request;
};

const getFilmApiCharacters = async () => {
  const response = await fetch(createRequest(url));
  const data = await response.json();
  return data.characters;
};

const getFilmCharacters = async () => {
  const charactersApi = await getFilmApiCharacters();
  charactersApi.forEach(async (characterApi) => {
    const response = await fetch(createRequest(characterApi));
    const data = await response.json();
    console.log(data.name);
  });
};

getFilmCharacters();
