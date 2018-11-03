from flask import Flask
from flask import render_template, request
from SearchTweets import buildquerydataforsearch
from UserTimeline import buildquerydataforusertimeline
from Friendships_create import buildquerydataforfriendshipscreate
from DirectMessage import buildquerydatafordirectmessage
from Tweet import buildtweet
from UsersLookup import buildlookup
from DeleteTweet import builddeletetweet
from Trends import buildtrendsquery


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

# Code by Matt
# rendering direct message
@app.route('/FriendShipsCreate/')
def friendshipscreate():
    return render_template('Friendships_create.html')

# calling the user timeline api which returns the most recent Tweets by the user based on query parameters.


@app.route('/FriendShipsCreateUsingParams', methods=['POST'])
def friendshipscreateusingparams():
        return buildquerydataforfriendshipscreate(request.form)

# Code by Matt
# rendering Direct message
@app.route('/DirectMessage/')
def directmessage():
    return render_template('DirectMessage.html')

# calling the user timeline api which returns the most recent Tweets by the user based on query parameters.


@app.route('/DirectMessageUsingParams', methods=['POST'])
def directmessageusingparams():
    return buildquerydatafordirectmessage(request.form)


# Code by Jonathan
# rendering Tweet
@app.route('/Tweet/')
def updatestatus():
    return render_template('Tweet.html')

# calling the user timeline api which returns the most recent Tweets by the user based on query parameters.


@app.route('/TweetUsingParam', methods=['POST'])
def updatestatususingparams():
    return buildtweet(request.form)

# Code by Jonathan
# rendering Tweet
@app.route('/DeleteTweet/')
def deletetweet():
    return render_template('DeleteTweet.html')

# calling the user timeline api which returns the most recent Tweets by the user based on query parameters.


@app.route('/DeleteTweetUsingParam', methods=['POST'])
def deletetweetusingparams():
    return builddeletetweet(request.form)


# Code by Emmeline
# rendering Users Lookup
@app.route('/UsersLookup/')
def userslookup():
    return render_template('UsersLookup.html')

# calling the users lookup api that would return the user(s) based on the query parameters

@app.route('/UsersLookupUsingParam', methods=['POST'])
def builduserslookup():
        return buildlookup(request.form)

# Code by Sindhuja
# rendering Users Lookup
@app.route('/Trends/')
def trends():
    return render_template('Trends.html')

# calling the users lookup api that would return the user(s) based on the query parameters

@app.route('/TrendsUsingParams', methods=['POST'])
def buildtrends():
        return buildtrendsquery(request.form)
