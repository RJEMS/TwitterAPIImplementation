from flask import Flask
from flask import render_template, request
from SearchTweets import searchresults
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('Index.html')

@app.route('/TwitterApi/')
def callingtwitterapi():
    return render_template('Index.html')


@app.route('/Search/')
def search():
    return render_template('SearchTweets.html')


@app.route('/SearchUsingParams', methods=['POST'])
def searchbyparam():
    return json.dumps(searchresults(request.form))


