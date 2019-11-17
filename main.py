import collage
import collage_twitter
import json
import os

def get_creds():
    """Receive the credentials from creds.json"""
    with open("creds.json") as f:
        return json.load(f)

if __name__ == "__main__":
    creds = get_creds()
    collage.save_wk(creds['lastfm-user'])
    api = collage_twitter.access_api(creds)
    tweeted = collage_twitter.send_tweet(api)
    if tweeted:
        os.remove("lastfmcollage.jpg")