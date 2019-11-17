from datetime import datetime
import twitter

def get_date():
    """Creates a DD/MM/YYYY datestamp"""
    return datetime.now().strftime("%d/%m/%Y")

def access_api(creds):
    """Accesses the Twitter API through python-twitter"""
    return twitter.Api(consumer_key=creds['twitter-api'],
                      consumer_secret=creds['twitter-api-secret'],
                      access_token_key=creds['twitter-access'],
                      access_token_secret=creds['twitter-access-secret'])

def send_tweet(api):
    """Sends a tweet of the collage"""
    try:
        api.PostUpdate(get_date(), media="lastfmcollage.jpg")
        return True
    except:
        return False