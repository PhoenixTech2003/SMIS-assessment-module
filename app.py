from flask import Flask, render_template, request
import _mysql_connector

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")