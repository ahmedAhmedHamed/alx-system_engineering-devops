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
    r = requests.get('https://www.reddit.com/r/{}/about.json'.format(subreddit))
    json_data = json.loads(r.text)
    return json_data['data']['subscribers']
