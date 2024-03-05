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
    request_str = f'https://www.reddit.com/r/{subreddit}/search'
    response = requests.get(request_str,
                    headers=headers,
                    allow_redirects=False,
                    timeout=1000
                    )
    if response.status_code != 200:
        print('None')
        return
    print(response.text)
    json_data = json.loads(response.text)
    out_file = open("myfile.json", 'w')
    json.dump(json_data, out_file, indent=4)
    out_file.close()
    print()

top_ten('python')
