// Assuming work_session_time is defined elsewhere and passed to this function
function setupCountdownTimer(minutes) {
  let timerElement = document.getElementById("countdown-timer");

  let totalTimeInSeconds = minutes * 60; // Convert minutes to seconds
  let timerInterval = null;

  function updateTimerDisplay() {
    let minutes = Math.floor(totalTimeInSeconds / 60);
    let seconds = totalTimeInSeconds % 60;

    // Format the time
    let formattedTime = `${minutes < 10 ? "0" : ""}${minutes}:${
      seconds < 10 ? "0" : ""
    }${seconds}`;
    timerElement.innerText = formattedTime; // Update the display
  }

  function startTimer() {
    // Prevent multiple intervals from being created
    if (timerInterval === null) {
      timerInterval = setInterval(function () {
        if (totalTimeInSeconds > 0) {
          totalTimeInSeconds--;
          updateTimerDisplay();
        } else {
          clearInterval(timerInterval);
          timerInterval = null; // Reset the timerInterval to allow restart
        }
      }, 1000);
    }
  }

  function pauseTimer() {
    if (timerInterval !== null) {
      clearInterval(timerInterval);
      timerInterval = null; // Pause the timer, without resetting the time
    }
  }

  function resetTimer() {
    totalTimeInSeconds = minutes * 60; // Reset the timer to its original value
    updateTimerDisplay(); // Update display to show reset time
  }

  // Initialize the timer display
  updateTimerDisplay();

  // Event listeners for the buttons
  document
    .getElementById("start-timer-btn")
    .addEventListener("click", startTimer);
  document
    .getElementById("pause-timer-btn")
    .addEventListener("click", pauseTimer);
  document
    .getElementById("reset-timer-btn")
    .addEventListener("click", resetTimer);
}

document.addEventListener("DOMContentLoaded", function () {
  // Invoke setupCountdownTimer with a duration of 2 minutes (120 seconds)
  setupCountdownTimer(2);
});
