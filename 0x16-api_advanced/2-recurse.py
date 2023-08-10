#!/usr/bin/python3
"""
This module takes a subreddit as an argument and returns the list of hot post
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if after:
        url += "?after={}".format(after)

    header = {"User-Agent": "project_subred"}

    res = requests.get(url, headers=header)

    if res.status_code == 200:
        data = res.json()
        children = data['data']['children']
        for post in children:
            hot_list.append(post['data']['title'])

        after = data['data']['after']
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
