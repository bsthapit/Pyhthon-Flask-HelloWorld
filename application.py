from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Earth! Bish here!!! Just trying to deploy my first app in Azure!!"
