from flask import Flask, render_template, request, redirect
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

GUESTBOOK_FILE = 'guestbook.txt'

def read_guestbook():
    entries = []
    try:
        with open(GUESTBOOK_FILE, 'r') as file:
            for line in file:
                name, message = line.strip().split("|")
                entries.append({"name": name, "message": message})
    except FileNotFoundError:
        pass
    return entries

def write_guestbook(name, message):
    with open(GUESTBOOK_FILE, 'a') as file:
        file.write(f"{name}|{message}\n")

@app.route('/')
def index():
    guestbook_entries = read_guestbook()
    return render_template('index.html', guestbook_entries=guestbook_entries)

@app.route('/guestbook', methods=['POST'])
def add_guestbook_entry():
    name = request.form.get('guestbook-name')
    message = request.form.get('guestbook-message')
    if name and message:
        write_guestbook(name, message)
        return redirect('/')
    return 'Name and message are required!', 400

if __name__ == '__main__':
    app.run(debug=True)