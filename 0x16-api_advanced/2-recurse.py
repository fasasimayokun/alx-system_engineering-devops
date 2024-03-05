#!/usr/bin/python3
"""a recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit. If no
results are found for the given subreddit, the function should return None."""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """a func that returns a list containing the titles of all hto articles"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Api_advanced/v1.0.0 (by /u/maykay_jr)"}
    params = {"after": after, "count": count, "limit": 100}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    res = response.json().get("data")
    after = res.get("after")
    count += res.get("dist")
    for ch in res.get("children"):
        hot_list.append(ch.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
