#!/usr/bin/python3
"""
this gets tasks from API and converts them to CSV
"""
import sys
import urllib.request
import json
import csv

if __name__ == "__main__":
    """
    talk to this using command line arguments
    """
    emp_id = sys.argv[1]
    query = f"?userId={emp_id}"
    todos = json.loads(urllib.request.urlopen(f"https://jsonplaceholder.typicode.com/todos{query}").read())
    users = json.loads(urllib.request.urlopen(f"https://jsonplaceholder.typicode.com/users{query}").read())
    username = None
    exportable_arr = []
    for user in users:
        if user["id"] == int(emp_id):
            username = user["username"]
            break

    for task in todos:
        exportable_arr.append([emp_id, username, task["completed"], task["title"]])
    with open(f'{emp_id}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerows(exportable_arr)
