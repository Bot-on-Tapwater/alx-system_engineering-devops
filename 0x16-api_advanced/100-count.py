#!/usr/bin/python3

"""Count keywords"""
import requests
from collections import Counter


def count_words(subreddit, word_list, after=None, counts=None):
    """Count keywords"""
    # Initialize counts dictionary if not provided
    if counts is None:
        counts = Counter()

    # Create the Reddit API URL
    base_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'your-user-agent'}

    # Make the API request
    response = requests.get(base_url, headers=headers, params={'after': after})

    # Check for valid subreddit
    if response.status_code != 200:
        if response.status_code == 302:
            print("Invalid subreddit or no posts found.")
        return

    # Parse the JSON response
    data = response.json()

    # Extract and count words in the titles
    for post in data['data']['children']:
        title = post['data']['title'].lower()
        for word in word_list:
            if title.count(word.lower()) > 0:
                counts[word.lower()] += title.count(word.lower())

    # Check for more pages
    if data['data']['after'] is not None:
        count_words(subreddit, word_list, data['data']['after'], counts)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".
              format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        keywords = [x.lower() for x in sys.argv[2].split()]
        count_words(subreddit, keywords)
