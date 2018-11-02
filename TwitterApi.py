from flask import Flask
from flask import render_template, request
from SearchTweets import buildquerydataforsearch
from UserTimeline import buildquerydataforusertimeline
import json

app = Flask(__name__)

# setting the route for the project
# rendering the home page


@app.route('/')
def index():
    return render_template('Index.html')


@app.route('/TwitterApiImplementation/')
def homepage():
    return render_template('Index.html')


@app.route('/Results')
def results():
    return render_template('Results.html')

# Code by Rajshree
# rendering the search page


@app.route('/Search/')
def search():
    return render_template('SearchTweets.html')

# calling the search api for finding the relevant Tweets based on queries performed by the users.


@app.route('/SearchUsingParams', methods=['POST'])
def searchusingparams():
        return buildquerydataforsearch(request.form)

# Code by Rajshree
# rendering the user timeline page


@app.route('/UserTimeline/')
def usertimeline():
    return render_template('UserTimeline.html')

# calling the user timeline api which returns the most recent Tweets by the user based on query parameters.


@app.route('/UserTimelineUsingParams', methods=['POST'])
def usertimelineusingparams():
        return buildquerydataforusertimeline(request.form)

