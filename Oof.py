from random import shuffle
import tweepy
import time
from auth import consumer_secret, consumer_key, access_token_secret, access_token


def main():

    twitter_auth_keys = {
        'consumer_secret': consumer_secret,
        'consumer_key': consumer_key,
        'access_token_secret': access_token_secret,
        'access_token': access_token
    }
    auth = tweepy.OAuthHandler(
        twitter_auth_keys['consumer_key'],
        twitter_auth_keys['consumer_secret']
    )
    auth.set_access_token(
        twitter_auth_keys['access_token'],
        twitter_auth_keys['access_token_secret']
    )
    api = tweepy.API(auth)

    starttime = time.time()
    with open('words.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    shuffle(lines)
    for line in lines:
        tweet = ('The {} oof.'.format(line))
        print('Tweeted: %s' % tweet)
        api.update_status(status=tweet)
        time.sleep(1800.0 - ((time.time() - starttime) % 1800.0))


if __name__ == '__main__':
    main()
