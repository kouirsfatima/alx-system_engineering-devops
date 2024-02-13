#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
import requests

def number_of_subscribers(subreddit):
    # Reddit API base URL
    base_url = "https://www.reddit.com/r/"
    headers = {"User-Agent": "Custom-User-Agent"}


    response = requests.get(base_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    else:
        return 0
