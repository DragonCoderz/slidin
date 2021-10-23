from logging import debug
from os import truncate
from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'date': 'this is a date',
        'title': 'Title: Blog Post 1',
        'user': 'I am this person',
        'content': 'content stuff'
    }
]

@app.route("/")
@app.route("/createProfile")
def createProfile():
    return render_template('createProfile.html', posts=posts)
@app.route("/search")
def search():
    return render_template('search.html')
if __name__ == '__main__':
    app.run(debug=True)
