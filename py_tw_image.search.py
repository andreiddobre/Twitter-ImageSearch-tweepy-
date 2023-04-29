from flask import Flask, render_template, request
import tweepy

# uplifting message
print("You got this!")

app = Flask(__name__)

# set up Twitter API credentials
API_key = "uILqR7AKhdlBmtzsb1yIgnxrI"
API_secret = "jAxcutigaWAFFtLSW37Uoi4czE8TYA1LPWkc7OW3Is0i91593y"
access_token = "919432051-pI7Uvsy9p3DZdC2Z36S5s30bLIyrMyd6PWuMZuIe"
access_token_secret = "VyD3vu0eST6V5NLfhLyhO0KtVI1e4ozQZYGzi9FmtiMcz"

# authenticate with Twitter API (setup the authentication handler and passing in all necessary access credentials)
auth = tweepy.OAuth1UserHandler(API_key, API_secret, access_token, access_token_secret)

# create tweepy API instance (so we can access the Twitter API with the provided authentication credentials)
api = tweepy.API(auth)

# verify credentials
try:
    api.verify_credentials()
    print("Authentication Successful")
except:
    print("Authentication Error")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # get the search term from the form
        search_term = request.form['search_term']
        
        # get the "only results with images" option from the form
        only_images = request.form.get('only_images')
        
        # set the number of tweets to retrieve
        num_tweets = 9
        
        # search for tweets containing the search term
        if only_images:
            tweets = api.search_tweets(q=search_term, count=num_tweets, tweet_mode='extended', include_entities=True, media_type='photo')
        else:
            tweets = api.search_tweets(q=search_term, count=num_tweets, tweet_mode='extended', include_entities=True)
        
        # render the template with the tweet texts
        return render_template('home.html', tweets=tweets, search_term=search_term, only_images=only_images)
    
    # if the request is a GET request, render the home.html template
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug = True)
