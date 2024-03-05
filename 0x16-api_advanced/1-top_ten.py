#!/usr/bin/python3
"""a function that queries the Reddit API and prints the titles of
the first 10 hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """a func that prints the titles of the 1st 10 hot posts in subreddti"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Api_advanced/v1.0.0 (by /u/maykay_jr)"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        res = response.json().get("data")
        for post in res.get("children")[:10]:
            print(post.get("data").get("title"))
    else:
        print("None")
