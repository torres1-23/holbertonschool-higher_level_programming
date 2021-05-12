/* Script that fetches the character name from this
URL: https://swapi-api.hbtn.io/api/people/5/?format=json
nad displays it in the header element */
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  $('DIV#character').text(data.name);
});
