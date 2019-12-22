$(document).on('click', '[id="update"]', function(){
  var btn = document.getElementById('update');
  $('#exampleModal #exampleModalLabel').text(btn.value);
  $('#exampleModal #exampleModalBody').text(btn.value + 'します。よろしいですか？');
  $('#exampleModal').modal('show')
}); 
$(document).on('click', '[id="submit"]', function(){
  $('#oyoyo_form').submit();
});

