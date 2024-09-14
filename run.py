from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello everyone my name is juswa ahha</p>"
