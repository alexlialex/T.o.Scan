// TODO: Recieve the python output and output the HTML file
document.getElementById("buttonscan").onclick = function() {myFunction()};

function myFunction() {
  //chrome.extension.getBackgroundPage().console.log('foo');
  $('#form').on('submit', function(e){
    e.preventDefault();
    $.ajax({
      type : 'POST',
      url : 'http://127.0.0.1:5000/urlStuff',
      contentType: "application/json",
      dataType: "text",
      data : JSON.stringify(
          {'urllink': 'https://www.apple.com/legal/internet-services/terms/site.html'}
      ),
      success : function(data) {
        document.getElementById("testtt").innerHTML = "SUMMARY COMPILED";
        console.log(data);
      },
      error : function(data){
        document.getElementById("testtt").innerHTML = "CANNOT GET DATA";
      }
    })
  })

}
