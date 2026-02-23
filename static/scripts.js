let currentButton = null;

function sendCommand(action) {

    fetch('/' + action)
        .then(res => res.json())
        .then(data => {

            updateStatus(action);
            highlightButton(action);

        })
        .catch(() => {
            document.getElementById("statusText").innerText = "ERROR";
            document.getElementById("statusText").style.color = "red";
        });
}

function updateStatus(action) {

    let text = action.toUpperCase();

    if (action === "stop") {
        text = "STOPPED";
        document.getElementById("statusText").style.color = "#ef4444";
    } else {
        document.getElementById("statusText").style.color = "#22c55e";
    }

    document.getElementById("statusText").innerText = text;
}

function highlightButton(action) {

    if (currentButton) {
        currentButton.classList.remove("active");
    }

    const btn = document.getElementById("btn-" + action);
    if (btn) {
        btn.classList.add("active");
        currentButton = btn;
    }
}

function setSpeed(value) {
    fetch("/speed", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ speed: value })
    });
}