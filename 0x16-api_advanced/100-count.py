#!/usr/bin/python3
""" a recursive function that queries the Reddit API, parses the title of
all hot articles, and prints a sorted count of given keywords
(case-insensitive, delimited by spaces. Javascript should
count as javascript, but java should not)."""
import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """a func that parses the title of all hot articles"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Api_advanced/v1.0.0 (by /u/maykay_jr)"}
    params = {"after": after, "count": count, "limit": 100}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    try:
        res = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        print('')
        return

    res = res.get("data")
    after = res.get("after")
    count += res.get("dist")
    for ch in res.get("children"):
        title = ch.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                times = lent([tl for tl in title if tl == word.lower()])
                if instances.get(word) is None:
                    instances[word] = times
                else:
                    instances[word] += times

    if after is None:
        if len(instances) == 0:
            print('')
            return
        instances = sorted(instances.items(), key=lambda ky: (-ky[1], ky[0]))
        [print("{}: {}".format(k, v)) for k, v in instances]
    else:
        count_words(subreddit, word_list, instances, after, count)
