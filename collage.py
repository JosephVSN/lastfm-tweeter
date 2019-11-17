import requests

COLLAGE_URL = "http://www.tapmusic.net/collage.php"

def req_img(lastfm_user, collage_type, size):
    """Creates the request for the image"""
    p = {
        'user': lastfm_user,
        'type': collage_type,
        'size': size
    }
    req = requests.get(COLLAGE_URL, params=p)
    if req.status_code != 200:
        print("Couldn't load page.")
    else:
        return req.content

def save_wk(lastfm_user):
    """Saves the 'week' collage's image locally"""
    img_cont = req_img(lastfm_user, "7day", "3x3")
    with open("lastfmcollage.jpg", "wb") as f:
        f.write(img_cont)
