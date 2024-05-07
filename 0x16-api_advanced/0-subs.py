#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit.

    If the subreddit is invalid and leads to a redirect (commonly to a search results page), return 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyRedditClient/1.0"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            # This includes any response code that isn't 200, e.g., 301, 302, 404, etc.
            return 0
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return 0
