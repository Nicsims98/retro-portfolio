from flask import Flask, render_template, request, redirect
from flask_cors import CORS

app = Flask(__name__, static_url_path='/static')

# Enable CORS globally
CORS(app, resources={
    r"/*": {  # Apply to all routes
        "origins": "*",  # Allow all origins (you can replace "*" with specific URLs)
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Authorization", "Content-Type", "X-Requested-With"]
    }
})

# Route for the homepage
@app.route('/')
def index():
    guestbook_entries = []  # Disable guestbook entries (since Vercel has a read-only file system)
    return render_template('index.html', guestbook_entries=guestbook_entries)

# Route for the guestbook form submission
@app.route('/guestbook', methods=['POST'])
def add_guestbook_entry():
    # This will not save to a file to prevent 500 errors
    name = request.form.get('guestbook-name')
    message = request.form.get('guestbook-message')
    print(f"Received entry: {name} - {message}")
    return redirect('/')

# Main app runner
if __name__ == '__main__':
    app.run(debug=True, port=5000)
