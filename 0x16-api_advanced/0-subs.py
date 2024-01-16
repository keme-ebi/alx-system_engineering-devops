#!/usr/bin/python3
"""this module queries the reddit api"""

import json
import requests


def number_of_subscribers(subreddit):
    """queries the reddit api and returns the total number of subcribers
    for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {'User-Agent': 'Remmy'}
    # get the url
    req = requests.get(url, headers=header)
    if req.status_code != 200:
        return 0
    else:
        data = req.json()
        subs = data.get('data').get('subscribers')
        return subs
