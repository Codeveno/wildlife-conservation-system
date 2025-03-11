document.getElementById("detectionForm").addEventListener("submit", async function (e) {
    e.preventDefault();
    const imageInput = document.getElementById("imageInput").files[0];

    const formData = new FormData();
    formData.append("image_path", imageInput.name);

    const response = await fetch('/detection/detect', {
        method: 'POST',
        body: formData
    });

    const data = await response.json();
    const resultsDiv = document.getElementById("detection-results");
    resultsDiv.innerHTML = `<pre>${JSON.stringify(data.detections, null, 2)}</pre>`;
});

document.getElementById("fetchRecordsBtn").addEventListener("click", async function () {
    const response = await fetch('/insights/records');
    const data = await response.json();

    const recordsDiv = document.getElementById("tracking-records");
    recordsDiv.innerHTML = `<pre>${JSON.stringify(data.records, null, 2)}</pre>`;
});

document.getElementById("loginForm").addEventListener("submit", function (e) {
    e.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    if (username === "admin" && password === "password123") {
        window.location.href = "dashboard.html";
    } else {
        document.getElementById("login-error").textContent = "Invalid credentials. Try again.";
    }
});
