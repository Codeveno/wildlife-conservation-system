// scripts.js
document.addEventListener("DOMContentLoaded", function () {
    // Example: Update live video feed
    const liveFeed = document.getElementById("live-feed");
    if (liveFeed) {
        liveFeed.src = "{{ url_for('static', filename='images/live_feed.mp4') }}";
    }
});