import tweepy
from time import sleep
from config import *

# load api stuff from config
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


# ask the user what they want to do then runs the function accordingly
def mainlloop():
    while (True):
        try:
            for friend in tweepy.Cursor(api.friends).items():
                api.destroy_friendship(friend.id)
                print(friend.id)
        except tweepy.TweepError, e:
            if (e[0][0]['code'] == 88):
                print ('Rate Limit... sleeping for 5 minutes..')
                sleep(60 * 5)


if __name__ == "__main__":
    mainlloop()
