#!/usr/bin/python3
"""
this gets tasks from API and converts them to CSV
"""
import json
import urllib.request

if __name__ == "__main__":
    """
    talk to this using command line arguments
    """
    users =\
        (json.
         loads(urllib.request.urlopen(
            f"https://jsonplaceholder.typicode.com/users").read()))
    username = None
    exported_json = {}
    for user in users:
        exportable_arr = []
        username = user["username"]
        user_id = user["id"]
        query_string =\
            f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
        todos = json.loads(urllib.request.urlopen(query_string).read())
        for task in todos:
            exportable_arr.append({"task": task["title"],
                                   "completed": task["completed"],
                                   "username": username})
        exported_json[user_id] = exportable_arr
    with open(f"{'todo_all_employees'}.json", "w") as outfile:
        json.dump(exported_json, outfile)
