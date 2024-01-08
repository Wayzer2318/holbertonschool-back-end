#!/usr/bin/python3
"""returns information about todo list"""

import requests
from sys import argv


if __name__ == '__main__':
    users = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".
        format(argv[1])).json()
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".
        format(argv[1])).json()
    titles = []
    for task in todos:
        if task.get('completed') is True:
            titles.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(users.get('name'), len(titles), len(todos)))
    print("\n".join("\t {}".format(task) for task in titles))
