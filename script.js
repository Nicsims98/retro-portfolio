document.addEventListener("DOMContentLoaded", () => {
    // Easter Egg Typewriter Effect
    document.getElementById("easter-egg-button").addEventListener("click", () => {
        const message = "Have a better day than Fred Durst after Woodstock '99.";
        const displayArea = document.getElementById("secret-message");
        let i = 0;

        displayArea.textContent = ""; // Clear existing text
        displayArea.classList.remove("hidden");

        function typeWriterEffect() {
            if (i < message.length) {
                displayArea.textContent += message.charAt(i);
                i++;
                setTimeout(typeWriterEffect, 100);
            }
        }
        typeWriterEffect();
    });

    // Guestbook Entries Animation
    const form = document.getElementById("guestbook-form");
    const entriesList = document.getElementById("guestbook-entries");

    form.addEventListener("submit", (e) => {
        e.preventDefault();
        const name = document.getElementById("guestbook-name").value;
        const message = document.getElementById("guestbook-message").value;

        const entry = document.createElement("li");
        entry.innerHTML = `<strong>${name}</strong>: ${message}`;
        entry.style.color = "lime";
        entry.style.animation = "fadeIn 1s ease-in";

        entriesList.appendChild(entry);

        // Clear the form
        form.reset();
    });
});

// Sparkling Cursor Trail
document.addEventListener("mousemove", function (e) {
    const sparkle = document.createElement("div");
    sparkle.className = "sparkle";
    sparkle.style.left = `${e.pageX}px`;
    sparkle.style.top = `${e.pageY}px`;
    document.body.appendChild(sparkle);

    setTimeout(() => {
        sparkle.remove();
    }, 1000); // Sparkle disappears after 1 second
});

// Random GIF Popups
const gifs = [
    "/static/gifs/arrow.gif",
    "/static/gifs/barflower2.gif",
    "/static/gifs/skull.gif",
    "/static/gifs/flyingdragons.gif",
    "/static/gifs/cowbell.gif",
    "/static/gifs/bye.gif"
];

function randomGifPopup() {
    const randomGif = gifs[Math.floor(Math.random() * gifs.length)];
    const gifElement = document.createElement("img");
    gifElement.src = randomGif;
    gifElement.className = "floating-gif";
    gifElement.style.left = `${Math.random() * window.innerWidth}px`;
    gifElement.style.top = `${Math.random() * window.innerHeight}px`;
    document.body.appendChild(gifElement);

    setTimeout(() => {
        gifElement.remove();
    }, 3000); // Remove GIF after 3 seconds
}

// Show a random GIF every 5 seconds
setInterval(randomGifPopup, 5000);

// Page Load Animation
window.onload = function () {
    const welcomeMessage = document.createElement("div");
    welcomeMessage.id = "welcome-message";
    welcomeMessage.innerHTML = `
        <h1>Welcome to the RAD 90's Experience!</h1>
        <p>Prepare for a blast from the past 🚀</p>
    `;
    document.body.appendChild(welcomeMessage);

    setTimeout(() => {
        welcomeMessage.style.opacity = 0;
        setTimeout(() => {
            welcomeMessage.remove();
        }, 1000); // Remove after fading out
    }, 3000); // Show for 3 seconds
};

document.addEventListener("DOMContentLoaded", () => {
    // Easter Egg Typewriter Effect
    document.getElementById("easter-egg-button").addEventListener("click", () => {
        const message = "Have a better day than Fred Durst after Woodstock '99.";
        const displayArea = document.getElementById("secret-message");
        let i = 0;

        displayArea.textContent = ""; // Clear existing text
        displayArea.classList.remove("hidden");

        function typeWriterEffect() {
            if (i < message.length) {
                displayArea.textContent += message.charAt(i);
                i++;
                setTimeout(typeWriterEffect, 100);
            }
        }
        typeWriterEffect();
    });

    // Guestbook Entries Animation
    const form = document.getElementById("guestbook-form");
    const entriesList = document.getElementById("guestbook-entries");

    form.addEventListener("submit", (e) => {
        e.preventDefault();
        const name = document.getElementById("guestbook-name").value;
        const message = document.getElementById("guestbook-message").value;

        const entry = document.createElement("li");
        entry.innerHTML = `<strong>${name}</strong>: ${message}`;
        entry.style.color = "lime";
        entry.style.animation = "fadeIn 1s ease-in";

        entriesList.appendChild(entry);

        // Clear the form
        form.reset();
    });
});

// Sparkling Cursor Trail
document.addEventListener("mousemove", function (e) {
    const sparkle = document.createElement("div");
    sparkle.className = "sparkle";
    sparkle.style.left = `${e.pageX}px`;
    sparkle.style.top = `${e.pageY}px`;
    document.body.appendChild(sparkle);

    setTimeout(() => {
        sparkle.remove();
    }, 1000); // Sparkle disappears after 1 second
});

// Random GIF Popups
const gifs = [
    "/static/gifs/arrow.gif",
    "/static/gifs/barflower2.gif",
    "/static/gifs/skull.gif",
    "/static/gifs/flyingdragons.gif",
    "/static/gifs/cowbell.gif",
    "/static/gifs/bye.gif"
];

function randomGifPopup() {
    const randomGif = gifs[Math.floor(Math.random() * gifs.length)];
    const gifElement = document.createElement("img");
    gifElement.src = randomGif;
    gifElement.className = "floating-gif";
    gifElement.style.left = `${Math.random() * window.innerWidth}px`;
    gifElement.style.top = `${Math.random() * window.innerHeight}px`;
    document.body.appendChild(gifElement);

    setTimeout(() => {
        gifElement.remove();
    }, 3000); // Remove GIF after 3 seconds
}

// Show a random GIF every 5 seconds
setInterval(randomGifPopup, 5000);

// Page Load Animation
window.onload = function () {
    const welcomeMessage = document.createElement("div");
    welcomeMessage.id = "welcome-message";
    welcomeMessage.innerHTML = `
        <h1>Welcome to the RAD 90's Experience!</h1>
        <p>Prepare for a blast from the past 🚀</p>
    `;
    document.body.appendChild(welcomeMessage);

    setTimeout(() => {
        welcomeMessage.style.opacity = 0;
        setTimeout(() => {
            welcomeMessage.remove();
        }, 1000); // Remove after fading out
    }, 3000); // Show for 3 seconds
};
