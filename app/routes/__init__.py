from .. import app
from flask import render_template

from . import index

@app.route("/redirect/schulcloud")
def schulcloud():
    return render_template("schulcloud.html")