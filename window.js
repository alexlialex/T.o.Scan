function postData(input) {
    $.ajax({
        type: "POST",
        url: "~/script.py",
        data: { param: input },
        success: callbackFunc
    });
}

function callbackFunc(response) {
    // do something with the response
    console.log(response);
}

document.getElementById("button").onclick = function() {postData(window.location.href)}
