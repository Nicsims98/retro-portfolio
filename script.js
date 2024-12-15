document.addEventListener("DOMContentLoaded", () => {
    // Easter Egg Typewriter Effect
    const button = document.getElementById("easter-egg-button");
    const displayArea = document.getElementById("secret-message");

    button.addEventListener("click", () => {
        const message = "Have a better day than Fred Durst after Woodstock '99.";
        displayArea.textContent = ""; // Clear any existing message
        displayArea.classList.remove("hidden"); // Make sure the message is visible

        let i = 0;
        function typeWriterEffect() {
            if (i < message.length) {
                displayArea.textContent += message.charAt(i);
                i++;
                setTimeout(typeWriterEffect, 100);
            }
        }
        typeWriterEffect();
    });
});
