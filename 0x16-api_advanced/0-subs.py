#!/usr/bin/python3

"""Query number of subscribers for a subreddit"""

import requests


def number_of_subscribers(subreddit):
    """Query number of subscribers in subreddit"""

    # url link to the reddit api
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # send a GET request
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        subscribers = data["data"]["subscribers"]
        # print(subscribers)
        return (subscribers)

    else:
        print(f"Error: \
              Status code {response.status_code}.\
                  Response text: {response.text}")
        return (0)
