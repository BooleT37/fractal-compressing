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
    loadJSON('/static/encoded_data.json?_=' + Math.floor(Math.random() * 100000000), renderJson);
    var jsonBlock = document.getElementById("json");
    if (jsonBlock) {
        document.getElementById('toggleJson').addEventListener("click", onJsonToggle.bind(null, jsonBlock));
    }
    const targetImage = document.getElementById('target_image');
    const submitTargetImageButton = document.getElementById('submit_target_image');

    if (targetImage.files.length > 0) {
        submitTargetImageButton.disabled = null;
    }
    targetImage.addEventListener('change', function (e) {
        submitTargetImageButton.disabled = null;
    });

    const blankImage = document.getElementById('blank_image');
    const submitBlankImageButton = document.getElementById('submit_blank_image')

    if (blankImage.files.length > 0) {
        submitBlankImageButton.disabled = null;
    }

    blankImage.addEventListener('change', function (e) {
        submitBlankImageButton.disabled = null;
    });
}

function renderJson(json) {
    var jsonBlock = document.getElementById("json");
    if (jsonBlock) {
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