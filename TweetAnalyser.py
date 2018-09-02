import tweepy
from textblob import TextBlob
import sys
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

# Step 1 - Authenticate
consumer_key = 'quH6QIYZbqK52R4MzZnPiojcX'
consumer_secret = 'm9o6w3nVj5qLmB73KT8IBnQ2QploQlMezjpdpX8zoZSqnq3gac'

access_token = '977978269478850560-kX1u41nPgNjV3cAYla78Yi0iqwPda8o'
access_token_secret = 'GabQMmfziEMJBszaOICiHtr0Sn2OrLWdEjFHuGiPExtcc'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
x = input("Enter the keyword:  ")
public_tweets = api.search(x)



#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment
#You can decide the sentiment polarity threshold yourself


for tweet in public_tweets:
    print(tweet.text.translate(non_bmp_map))

    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
