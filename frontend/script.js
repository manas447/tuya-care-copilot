async function analyze() {
    const deviceId = document.getElementById("deviceId").value;
    const output = document.getElementById("output");

    output.innerText = "Analyzing...";

    const response = await fetch("http://127.0.0.1:8000/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            device_id: deviceId
        })
    });

    const data = await response.json();
    output.innerText = JSON.stringify(data, null, 2);
}
