#!/usr/bin/python3
"""
this gets the todos from an API
"""
import sys
import urllib.request
import json

if __name__ == "__main__":
    """
    talk to this using command line arguments
    """
    emp_id = sys.argv[1]
    query = f"?userId={emp_id}"
    todos = json.loads(urllib.request.urlopen(f"https://jsonplaceholder.typicode.com/todos{query}").read())
    users = json.loads(urllib.request.urlopen(f"https://jsonplaceholder.typicode.com/users{query}").read())
    username = None
    for user in users:
        if user["id"] == int(emp_id):
            username = user["name"]
            break
    number_completed = 0
    for todo in todos:
        if todo["completed"]:
            number_completed += 1
    print(f"Employee {username} is done with tasks({len(todos) - number_completed}/{len(todos)}):")
    for task in todos:
        print(f"\t {task['title']}")
