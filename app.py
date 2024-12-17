from flask import Flask, render_template, request, redirect
from flask_cors import CORS
import logging

# Initialize Flask app
app = Flask(__name__, static_folder='static', template_folder='templates')

# Enable CORS globally
CORS(app, resources={
    r"/*": {
        "origins": "*",  # Allow all origins; replace "*" with specific URLs if needed
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Authorization", "Content-Type", "X-Requested-With"]
    }
})

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Replace file-based guestbook with in-memory list
guestbook_entries = []  # Temporary in-memory storage


# Function to read guestbook entries
def read_guestbook():
    return guestbook_entries


# Function to write new guestbook entries
def write_guestbook(name, message):
    guestbook_entries.append({"name": name, "message": message})
    app.logger.info(f"Added guestbook entry: {name} - {message}")


# Route for homepage
@app.route('/')
def index():
    try:
        guestbook_entries_list = read_guestbook()  # Load guestbook entries
        return render_template('index.html', guestbook_entries=guestbook_entries_list)
    except Exception as e:
        app.logger.error(f"Error in '/' route: {e}")
        return "An internal server error occurred.", 500


# Route for handling guestbook submissions
@app.route('/guestbook', methods=['POST'])
def add_guestbook_entry():
    try:
        name = request.form.get('guestbook-name')
        message = request.form.get('guestbook-message')

        if name and message:
            write_guestbook(name, message)
            return redirect('/')
        else:
            return "Both name and message are required.", 400
    except Exception as e:
        app.logger.error(f"Error in '/guestbook' route: {e}")
        return "An internal server error occurred.", 500


# Main app runner
if __name__ == '__main__':
    app.run(debug=True, port=5000)
