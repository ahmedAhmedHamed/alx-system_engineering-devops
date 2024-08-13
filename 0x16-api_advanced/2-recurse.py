#!/usr/bin/python3
"""
houses recurse, which returns a list containing
all the titles of all hot articles of a given subreddit
"""

import json
import requests


def recurse(subreddit, hot_list=[]):
    """
    returns all the titles of all hot articles of a given subreddit
    or None.
    """
    headers = {'User-Agent': 'hamed_useragent'}
    request_str = f'https://www.reddit.com/r/{subreddit}/hot.json'
    payload = {
        "limit": 8,
    }
    response = requests.get(request_str,
                            headers=headers,
                            allow_redirects=False,
                            params=payload,
                            timeout=1000
                            )
    if response.status_code != 200:
        return None
    return
