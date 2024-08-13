#!/usr/bin/python3
"""
this module prints the top ten posts of a subreddit
"""

import json
import requests


def top_ten(subreddit):
    """
    prints top ten posts from subreddit
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
        print('None')
        return
    json_data = json.loads(response.text)
    for child in json_data['data']['children']:
        print(child['data']['title'])
