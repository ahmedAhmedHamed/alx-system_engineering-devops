#!/usr/bin/python3
"""
this module queries the reddit api for the number of subscribers of a subreddit
"""
import json
import requests


def number_of_subscribers(subreddit):
    """
    gets the number of subscribers of a subreddit
    """
    headers = {'User-Agent': 'hamed_useragent'}
    request_str = f'https://www.reddit.com/r/{subreddit}/about.json'
    r = requests.get(
        request_str,
        allow_redirects=False,
        headers=headers,
        timeout=1000
        )

    if r.status_code != 200:
        return '0'
    json_data = json.loads(r.text)
    return json_data['data']['subscribers']
