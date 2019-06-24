from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.static_folder = 'static'

client = MongoClient('mongo', 27017)
db = client.tododb

@app.route('/')
def todo():
    return render_template('index.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
