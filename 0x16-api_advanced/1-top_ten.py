#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""

    base_url = "https://www.reddit.com/r/"
    headers = {"User-Agent": "Custom-User-Agent"}
    response = requests.get(base_url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
