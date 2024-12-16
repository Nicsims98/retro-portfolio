document.addEventListener("DOMContentLoaded", () => {
    // Easter Egg Typewriter Effect
    document.getElementById("easter-egg-button").addEventListener("click", () => {
        const message = "Have a better day than Fred Durst after Woodstock '99!";
        const displayArea = document.getElementById("secret-message");
        let i = 0;

        displayArea.textContent = "";
        displayArea.classList.remove("hidden");

        function typeWriter() {
            if (i < message.length) {
                displayArea.textContent += message.charAt(i);
                i++;
                setTimeout(typeWriter, 50);
            }
        }
        typeWriter();
    });

    // Sparkling Cursor
    document.addEventListener("mousemove", (e) => {
        const sparkle = document.createElement("div");
        sparkle.className = "sparkle";
        sparkle.style.left = `${e.pageX}px`;
        sparkle.style.top = `${e.pageY}px`;
        document.body.appendChild(sparkle);

        setTimeout(() => sparkle.remove(), 1000);
    });
});
