<<<<<<< HEAD
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# File to store guestbook entries
GUESTBOOK_FILE = 'guestbook.txt'

# Function to read the guestbook entries
def read_guestbook():
    entries = []
    try:
        with open(GUESTBOOK_FILE, 'r') as f:
            for line in f:
                name, message = line.strip().split("|")
                entries.append({'name': name, 'message': message})
    except FileNotFoundError:
        pass  # If the file doesn't exist, return an empty list
    return entries

# Function to write a new entry to the guestbook
def write_guestbook(name, message):
    with open(GUESTBOOK_FILE, 'a') as f:
        f.write(f"{name}|{message}\n")

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

if __name__ == '__main__':
    app.run(debug=True, port=5000)
=======
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# File to store guestbook entries
GUESTBOOK_FILE = 'guestbook.txt'

# Function to read the guestbook entries
def read_guestbook():
    entries = []
    try:
        with open(GUESTBOOK_FILE, 'r') as f:
            for line in f:
                name, message = line.strip().split("|")
                entries.append({'name': name, 'message': message})
    except FileNotFoundError:
        pass  # If the file doesn't exist, return an empty list
    return entries

# Function to write a new entry to the guestbook
def write_guestbook(name, message):
    with open(GUESTBOOK_FILE, 'a') as f:
        f.write(f"{name}|{message}\n")

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

if __name__ == '__main__':
    app.run(debug=True, port=5000)
>>>>>>> 42bad24b91e2f821d52b2d1698c2fb69f85657f9
