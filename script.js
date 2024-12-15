document.addEventListener("DOMContentLoaded", () => {
    const message = "Have a better day than Fred Durst after Woodstock '99.";
    const button = document.getElementById("easter-egg-button");
    const displayArea = document.getElementById("secret-message");

    button.addEventListener("click", () => {
        displayArea.textContent = "";
        displayArea.classList.remove("hidden");

        let i = 0;
        function typeWriter() {
            if (i < message.length) {
                displayArea.textContent += message.charAt(i);
                i++;
                setTimeout(typeWriter, 50);
            }
        }
        typeWriter();
    });
});