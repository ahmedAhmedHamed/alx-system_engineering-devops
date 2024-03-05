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
    r = requests.get('https://www.reddit.com/r/{}/about.json'.format(subreddit),
                      allow_redirects=False)

    if r.status_code!= 200:
        return 0

    try:
        json_data = json.loads(r.text)
    except json.decoder.JSONDecodeError:
        return 0

    return json_data['data']['subscribers']
