document.addEventListener("DOMContentLoaded", function () {
  let mode = "work"; // Initialize mode to "work"
  let remainingTime = 1500; // 25 minutes in seconds as default
  let isTimerRunning = false;
  let startTime;
  let endTime;
  let timerInterval = null;
  //const sound = new Audio('path_to_your_audio_file.mp3'); // Placeholder for your sound file

  function updateDisplay() {
    const minutes = Math.floor(remainingTime / 60);
    const seconds = remainingTime % 60;
    const formattedTime = `${minutes < 10 ? "0" : ""}${minutes}:${
      seconds < 10 ? "0" : ""
    }${seconds}`;

    // Update the countdown timer display
    document.getElementById("countdown-timer").textContent = formattedTime;

    // Update the browser tab's title with remaining time and mode
    document.title = `${
      mode.charAt(0).toUpperCase() + mode.slice(1)
    } time - ${formattedTime}`;
  }

  function calculateRemainingTime() {
    const currentTime = Date.now();
    const elapsedTime = Math.floor((currentTime - startTime) / 1000);
    return Math.max(endTime - elapsedTime, 0);
  }

  function switchMode(newMode) {
    mode = newMode || (mode === "work" ? "break" : "work");
    remainingTime = mode === "work" ? 1500 : 300; // 25 minutes for work, 5 minutes for break
    isTimerRunning = false;
    clearInterval(timerInterval);
    timerInterval = null;
    updateDisplay();
    // Update the HTML message
    document.getElementById(
      "mode-message"
    ).textContent = `${mode} timer is set. Ready to start!`;
  }

  function startTimer() {
    if (!isTimerRunning) {
      isTimerRunning = true;
      startTime = Date.now();
      endTime = remainingTime;
      timerInterval = setInterval(() => {
        remainingTime = calculateRemainingTime();
        if (remainingTime <= 0) {
          clearInterval(timerInterval);
          isTimerRunning = false;
          //sound.play(); // Play the sound alert
          // Display completion message
          document.getElementById(
            "mode-message"
          ).textContent = `${mode} timer done! Time for a ${
            mode === "work" ? "break" : "work"
          } session.`;
          switchMode(); // Optional: Automatically switch modes
        }
        updateDisplay();
      }, 1000);
    }
  }

  function pauseTimer() {
    if (isTimerRunning) {
      isTimerRunning = false;
      remainingTime = calculateRemainingTime();
      clearInterval(timerInterval);
    }
  }

  // Update to only reset if the timer is not running
  function resetTimer() {
    if (!isTimerRunning) {
      remainingTime = mode === "work" ? 1500 : 300;
      updateDisplay();
    }
  }

  document
    .getElementById("start-timer-btn")
    .addEventListener("click", startTimer);
  document
    .getElementById("pause-timer-btn")
    .addEventListener("click", pauseTimer);
  document
    .getElementById("reset-timer-btn")
    .addEventListener("click", resetTimer);
  document
    .getElementById("work-mode-btn")
    .addEventListener("click", () => switchMode("work"));
  document
    .getElementById("break-mode-btn")
    .addEventListener("click", () => switchMode("break"));

  updateDisplay(); // Initialize display with the default or current state
});
