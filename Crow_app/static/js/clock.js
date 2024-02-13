function updateClock() {
    var now = new Date();
    var hours = now.getHours();
    var minutes = now.getMinutes();
    var seconds = now.getSeconds();

    // Pad single digit hours, minutes, and seconds with leading zeros
    hours = (hours < 10 ? "0" : "") + hours;
    minutes = (minutes < 10 ? "0" : "") + minutes;
    seconds = (seconds < 10 ? "0" : "") + seconds;

    // Format the time as HH:MM:SS
    var timeString = hours + ":" + minutes + ":" + seconds;

    // Update the clock element with the current time
    document.getElementById("clock").innerHTML = timeString;
}

// Call updateClock every second
setInterval(updateClock, 1000);

// Initial call to display the clock immediately
updateClock();