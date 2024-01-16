#!/usr/bin/python3
"""this module queries the reddit api"""

import json
import requests


def top_ten(subreddit):
    """queries the reddit api and prints the title of the first 10
    hot posts listed for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    header = {'User-Agent': 'Remmy'}
    # get the url
    req = requests.get(url, headers=header, allow_redirects=False)
    if req.status_code != 200:
        print(None)
    else:
        data = req.json()
        child = data.get('data').get('children')
        for h_post in child[:10]:
            title = h_post.get('data').get('title')
            print(title)
