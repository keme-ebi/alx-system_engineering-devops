#!/usr/bin/python3
"""
This module takes a subreddit as an argument and returns the first 10 hot post
"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    header = {"User-Agent": "project_subred"}

    res = requests.get(url, headers=header)

    if res.status_code == 200:
        data = res.json()
        children = data['data']['children']
        for post in children:
            hot = post['data']['title']
            print(hot)
    else:
        print(None)
