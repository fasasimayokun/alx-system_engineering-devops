#!/usr/bin/python3
""" a recursive function that queries the Reddit API, parses the title of
all hot articles, and prints a sorted count of given keywords
(case-insensitive, delimited by spaces. Javascript should
count as javascript, but java should not)."""
import requests
from collections import Counter


def count_words(subreddit, word_list):
    """a func that parses the title of all hot articles"""
    return count_word_helper(
        subreddit=subreddit,
        word_list=word_list,
        after=None,
        word_counts=None
    )


def count_word_helper(subreddit, word_list, after, word_counts):
    """An util for the count_words function"""
    if word_counts is None:
        word_counts = Counter()
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"limit": 100, "after": after}
    response = requests.get(
        url, headers={"User-agent": "MyApiAdvanced/1.0"}, params=params)
    if response.status_code == 200:
        data = response.json()
        posts = data.get("data").get("children")
        for post in posts:
            title = post.get("data").get("title").lower()
            for word in word_list:
                word_counts[word.lower()] += title.count(word.lower())
        after = data.get("data").get("after")
        if after:
            return count_word_util(subreddit, word_list, after, word_counts)
        else:
            sorted_counts = sorted(word_counts.items(),
                                   key=lambda xy: (-xy[1], xy[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    else:
        return None
