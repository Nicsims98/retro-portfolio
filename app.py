from flask import Flask, render_template, request, redirect
from flask_cors import CORS  # Import CORS for handling cross-origin requests

app = Flask(__name__)

# Define allowed CORS configuration
frontend_origins = ["*"]  # Allow all origins; replace with a list of specific URLs if needed
cors_config = {
    r"*": {  # Match all routes
        "origins": frontend_origins,  # Allowed origins
        "methods": ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],  # Allowed HTTP methods
        "allow_headers": [  # Allowed headers in requests
            "Authorization",
            "Content-Type",
            "X-Requested-With",
            "X-CSRF-Token"
        ],
        "supports_credentials": True  # Allow cookies and authentication
    }
}

# Apply CORS to the app with the defined configuration
CORS(app, resources=cors_config)

# File to store guestbook entries
GUESTBOOK_FILE = 'guestbook.txt'

# Function to read guestbook entries
def read_guestbook():
    entries = []
    try:
        with open(GUESTBOOK_FILE, 'r') as file:
            for line in file:
                try:
                    name, message = line.strip().split("|")
                    entries.append({'name': name, 'message': message})
                except ValueError:
                    print(f"Skipping invalid line: {line.strip()}")
    except FileNotFoundError:
        pass
    return entries

# Function to write new entries
def write_guestbook(name, message):
    with open(GUESTBOOK_FILE, 'a') as file:
        file.write(f"{name}|{message}\n")

# Route for homepage
@app.route('/')
def index():
    guestbook_entries = read_guestbook()
    return render_template('index.html', guestbook_entries=guestbook_entries)

# Route for adding guestbook entries
@app.route('/guestbook', methods=['POST'])
def add_guestbook_entry():
    name = request.form.get('guestbook-name')
    message = request.form.get('guestbook-message')

    if name and message:
        write_guestbook(name, message)
        return redirect('/')
    else:
        return 'Both name and message are required.', 400

# Start the server
if __name__ == '__main__':
    app.run(debug=True, port=5000)
