from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, this is Heikos a sample Python Web App running on Flask Framework!"

