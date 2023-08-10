#!/usr/bin/python3
"""
This module takes an argmument that is a subreddit and returns the number
of subcribers for that subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {"User-Agent": "project_subred"}

    res = requests.get(url, headers=header)

    if res.status_code == 200:
        data = res.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
