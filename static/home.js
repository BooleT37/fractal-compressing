function loadJSON(filename, callback) {
    var xobj = new XMLHttpRequest();
        xobj.overrideMimeType("application/json");
    xobj.open('GET', filename, true);
    xobj.onreadystatechange = function () {
          if (xobj.readyState == 4 && xobj.status == "200") {
            callback(xobj.responseText);
          }
    };
    xobj.send(null);
}

function init() {
    loadJSON('/static/encoded_data.json', renderJson);
    var jsonBlock = document.getElementById("json");
    document.getElementById('toggleJson').addEventListener("click", onJsonToggle.bind(null, jsonBlock))
}

function renderJson(json) {
    var jsonBlock = document.getElementById("json");
    if (json) {
        jsonBlock.innerHTML = json;
    }
}

function onJsonToggle(jsonBlock) {
    var display = jsonBlock.style.display;
    if (display === "none" || display === "") {
        jsonBlock.style.display = "block";
    } else {
        jsonBlock.style.display = "none";
    }
}

window.addEventListener('DOMContentLoaded', init);