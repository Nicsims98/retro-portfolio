from flask import Flask, render_template, request, redirect
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# File to store guestbook entries
GUESTBOOK_FILE = 'guestbook.txt'

# Function to read the guestbook entries
def read_guestbook():
    entries = []
    try:
        with open(GUESTBOOK_FILE, 'r') as file:
            for line in file:
                # Try to split the line into name and message
                try:
                    name, message = line.strip().split("|")
                    entries.append({"name": name, "message": message})
                except ValueError:
                    # Skip lines that don't have the correct format
                    print(f"Skipping invalid line: {line.strip()}")
    except FileNotFoundError:
        # File does not exist yet, return an empty list
        pass
    return entries

# Function to write a new entry to the guestbook
def write_guestbook(name, message):
    with open(GUESTBOOK_FILE, 'a') as file:
        file.write(f"{name}|{message}\n")

# Route for the homepage
@app.route('/')
def index():
    guestbook_entries = read_guestbook()
    return render_template('index.html', guestbook_entries=guestbook_entries)

# Route to handle guestbook submissions
@app.route('/guestbook', methods=['POST'])
def add_guestbook_entry():
    name = request.form.get('guestbook-name')
    message = request.form.get('guestbook-message')

    if name and message:
        write_guestbook(name, message)
        return redirect('/')
    else:
        return 'Both name and message are required.', 400

# Main entry point
if __name__ == '__main__':
    app.run(debug=True, port=5000)

