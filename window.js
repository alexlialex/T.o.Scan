// TODO: Recieve the python output and output the HTML file
document.getElementById("buttonscan").onclick = function() {myFunction()};

function myFunction() {
  $('#form').on('submit', function(e){
    e.preventDefault();
    $.ajax({
      url: 'http://127.0.0.1:5000/urlStuff/',
      data: {'htmldata': htmldata},
      method: 'POST',
      success: function(data) {
        $('p').html();
      }
    })
  })
  document.getElementById("testtt").innerHTML = "YOU CLICKED ME!";
}
