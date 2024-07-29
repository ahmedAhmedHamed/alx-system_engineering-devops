#!/usr/bin/python3
"""
this gets the todos from an API
"""
import json
import sys
import urllib.request

if __name__ == "__main__":
    """
    talk to this using command line arguments
    """
    emp_id = sys.argv[1]
    query = f"?userId={emp_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos{query}"
    users_url = f"https://jsonplaceholder.typicode.com/users{query}"
    todos = json.loads(urllib.request.urlopen(todo_url).read())
    users = json.loads(urllib.request.urlopen(users_url).read())
    username = None
    for user in users:
        if user["id"] == int(emp_id):
            username = user["name"]
            break
    number_completed = 0
    for todo in todos:
        if todo["completed"]:
            number_completed += 1
    output = f"Employee {username} is done\
     with tasks({number_completed}/{len(todos)}):"
    print(output)
    for task in todos:
        if task["completed"]:
            print(f"\t {task['title']}")
