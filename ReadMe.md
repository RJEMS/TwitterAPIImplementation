# Team Members
Emmeline Tsen
Sindhuja Ramini
Matt DiPietro
Jonathan Gee
Rajshree Chauhan

# Run these commands from the project directory
export FLASK_APP=TwitterApi.py
export FLASK_DEBUG=1
flask run

# To execute unit tests found in Utils_Tests.py
python -m unittest Utils_Tests.Testing

#Steps
# 1 - Create html pages for the api you are implementing and add route to TwitterApi.py for rendering the html

# 2 - In Index.html page edit the href, id and name of your API

# 3 - Utils.py contains oauth_req function that would be used for calling all the twitter APIs by passing the required parameters


# 4 - Write a function in TwitterApi.py that would be called on button click of your html page and specify proper route
#Example - searchusingparams

# 5 - This function has the form post data. Create a build query data function and call the Utils.py function by passing the required parameters
# 6 - The result from the API is passed to javascript and shown as a popup/alert.
# 7 - Unit Test Case
# 8 - Deployment


### Put public key and private key in environment variable




