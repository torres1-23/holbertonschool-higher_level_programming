/* Script that fetches and prints how to say “Hello” depending on the language */
$('document').ready(function () {
  $('INPUT#btn_translate').click(function () {
    $.get(`https://www.fourtonfish.com/hellosalut/?lang=${$('INPUT#language_code').val()}`, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
