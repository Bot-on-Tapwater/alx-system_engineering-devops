#!/usr/bin/python3

"""Get 10 hot posts for a subreddit recursively"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """Get 10 hot posts for a subreddit recursively"""

    # url link to the reddit api
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # prevents 429 status code (Rate limit)
    headers = {"User-Agent": "Custom"}

    # retrieve only 10 results
    params = {"after": after}

    # send a GET request
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 200:
        # get http response and convert from json type
        data = response.json()

        hotposts = data['data']['children']

        for child in hotposts:
            hot_list.append(child['data']['title'])

        after = data['data']['after']

        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)

    else:
        return (None)
