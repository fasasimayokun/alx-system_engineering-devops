#!/usr/bin/python3
"""a recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit. If no
results are found for the given subreddit, the function should return None."""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """a func that returns a list containing the titles of all hto articles"""
    return recurse_func(subreddit=subreddit, hot_list=hot_list, after=None)


def recurse_func(subreddit, hot_list=[], after=None):
    """An util for the recurse function"""
    if not hot_list:
        hot_list = []
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"limit": 100, "after": after}
    response = requests.get(
        url, headers={"User-agent": "MyApiAdavanced/1.0"}, params=params)
    if response.status_code == 200:
        data = response.json()
        posts = data.get("data").get("children")
        for post in posts:
            hot_list.append(post.get("data").get("title"))
        after = data.get("data").get("after")
        if after:
            return recurse_util(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
