from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.static_folder = 'static'


@app.route('/')
def todo():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
