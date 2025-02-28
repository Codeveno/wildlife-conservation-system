// scripts.js
document.addEventListener("DOMContentLoaded", function () {
    //Update live video feed
    const liveFeed = document.getElementById("live-feed");
    if (liveFeed) {
        liveFeed.src = "{{ url_for('static', filename='images/live_feed.mp4') }}";
    }
});
document.addEventListener("DOMContentLoaded", function() {
    let video = document.getElementById("background-video");
    video.playbackRate = 0.5; 
});
