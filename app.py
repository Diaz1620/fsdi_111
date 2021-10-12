from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello, world!<h1>"

@app.route("/about")
def about_me():
    me={
        "first_name": "Yadiel",
        "last_name": "DR",
        "hobbies": "Cooking",
        "active": True
    }
    return me