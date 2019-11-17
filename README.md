# lastfm-tweeter

Python automation to tweet out a Last.fm collage.

## Getting Started

TODO

### Prerequisites

TODO

## Deployment

The script requires a JSON which includes the user's Last.fm username, and Twitter API keys. The following is the format of the JSON:

```
{
    'lastfm-user': Last.fm username,
    'twitter-api': Twitter Consumer API Key,
    'twitter-api-secret': Twitter Consumer API Secret,
    'twitter-access': Twitter Access API Key,
    'twitter-access-secret': Twitter Access API Secret
}
```

This JSON should be built in the directory of the clone (assuming you're building off a clone of this repository).

There are numerous ways to deploy this as automation, the route I used was setting a crontab on my Rapsberry Pi to kick off the script.
More help on building a Twitter app can be found in the python-twitter [documentation](https://python-twitter.readthedocs.io/en/latest/getting_started.html).


## Built With

* [tapmusic Last.fm collager](http://www.tapmusic.net/) - Where the script get's the collages from
* [python-twitter](https://github.com/bear/python-twitter) - How the script interacts with Twitter

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


## Acknowledgments

* The team who built the [tapmusic](http://www.tapmusic.net/) Last.fm collage creator
* The [python-twitter](https://github.com/bear/python-twitter) library

