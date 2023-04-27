from flask import Flask, render_template, request
import tweepy
import os

app = Flask(__name__)

# set up Twitter API credentials
API_key = "GhBNuW6jZ6ZBuYhE6IKAxQ8k6"
API_secret = "RgbR1K2tt0BQdp0KoALjvk3u1tG9yhdnymlos1D2wsT4r0PNlp"
access_token = "571966749-PldY6PPm43TJDo00oZEE69fI7WK5AL3HigSgqWah"
access_token_secret = "ePxvcxTvBcjqMvYXorEDaxvSLi3LzYnxh2i5v54Ptf8v3"

# authenticate with Twitter API (setup the authentication handler and passing in all necessary access credentials)
auth = tweepy.OAuthHandler(API_key, API_secret)
auth.set_access_token(access_token, access_token_secret)

# create tweepy API instance (so we can access the Twitter API with the provided authentication credentials)
api = tweepy.API(auth)

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
            tweets = api.search(q=search_term, count=num_tweets, tweet_mode='extended', include_entities=True, media_type='photo')
        else:
            tweets = api.search(q=search_term, count=num_tweets, tweet_mode='extended', include_entities=True)
        
        # store the tweets in a list
        tweet_texts = []
        for tweet in tweets:
            tweet_text = tweet.full_text
            entities = tweet.entities
            if entities.get('media'):
                media_url = entities.get('media')[0]['media_url']
            else:
                media_url = None
            tweet_texts.append({'text': tweet_text, 'media_url': media_url})

        # render the template with the tweet texts
        return render_template('home.html', tweet_texts=tweet_texts, search_term=search_term, only_images=only_images)
    
    # if the request is a GET request, render the home.html template
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug = True)

