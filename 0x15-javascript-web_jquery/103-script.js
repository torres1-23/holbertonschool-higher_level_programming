/* Script that fetches and prints how to say “Hello” depending on the language */
$('document').ready(function () {
  $('INPUT#btn_translate').click(function () {
    $.get(`https://www.fourtonfish.com/hellosalut/?lang=${$('INPUT#language_code').val()}`, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
  $('INPUT#language_code').focus(function () {
    $(this).keydown(function (event) {
      if (event.keyCode === 13) {
        $.get(`https://www.fourtonfish.com/hellosalut/?lang=${$('INPUT#language_code').val()}`, function (data) {
          $('DIV#hello').text(data.hello);
        });
      }
    });
  });
});
