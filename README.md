Twitter image search using (tweepy+flask)

I have created this project following the requested tasks:
1.The app should be able to search either Facebook or Twitter API for a search term. Results get
stored in memory
2.Data fetched from the search is presented in a user-friendly way in the browser (up to you how).
3.Create an option around the search input that “only results with images” is desired. Display results
that include an image to the user.

Following the requirements, I used Flask web framework due to it's easy to expand feature and I chose Twitter API being easier to work with. I imported the required modules (tweety, flask), setup the Twitter authentication handler ans passing it all the acces credentials, created an tweepy API instance to acces Twitter API with the specified credentials.
I have created a search form in the front-end (templates/home.html) that once is submitted, it passed the search_term to the back-end, stored in the 'search' variable (the variable contains the user input) and the 'only_images' variable that gets the values from the form. I defined a maximum number of 9 tweets to retrieve, search for tweets given the search term, store them in a list 'tweet_texts'.
Up next, i render the template and pass the list results to home.html, customized by bootstrap to lookalike more with Twitter interface.

I also used an active virtual enviroment on Windows (command prompt: dev-env\bin\activate.bat) to "pip install flask" and "pip install tweepy", to help me generate a "pip freeze > requirements.txt", for any user running this script to easily run "pip install -r requirements.txt" so that all the required libraries install at once

