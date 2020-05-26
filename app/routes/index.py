from . import app
from flask import render_template, url_for
from datetime import datetime

# For testing only
posts = [
    {
        "author": "Elia",
        "content": "Hello World! \n This is a simple Test.",
        "time": datetime(2020, 5, 26, 16, 00)
    },
    {
        "author": "Tobi",
        "content": "Hi Leude!... btw REIN",
        "time": datetime(2020, 5, 26, 16, 30)
    },
    {
        "author": "Tobi",
        "content": "Hi Leude!... btw REIN",
        "time": datetime(2020, 5, 26, 16, 30)
    },
    {
        "author": "Tobi",
        "content": "Hi Leude!... btw REIN",
        "time": datetime(2020, 5, 26, 16, 30)
    },
    {
        "author": "Tobi",
        "content": "Hi Leude!... btw REIN",
        "time": datetime(2020, 5, 26, 16, 30)
    },
    {
        "author": "Tobi",
        "content": "Hi Leude!... btw REIN",
        "time": datetime(2020, 5, 26, 16, 30)
    },
    {
        "author": "Tobi",
        "content": "Hi Leude!... btw REIN",
        "time": datetime(2020, 5, 26, 16, 30)
    }
]

@app.route("/")
def index():
    return render_template("index.html", posts=posts, title="Home")