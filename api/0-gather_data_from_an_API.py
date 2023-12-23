#!/usr/bin/python3
"""
get data from a API
"""
import sys
import requests


if __name__ == "__main__":
    id = sys.argv[1]
    completed = 0
    total = 0
    tasks = []
    url_user = "https://jsonplaceholder.typicode.com/users/" + id
    user = requests.get(url_user).json()
    name = user.get("name")
    todos = "https://jsonplaceholder.typicode.com/todos/"
    task_list = requests.get(todos).json()

    for task in task_list:
        if task.get("userId") == int(id):
            if task.get("completed") is True:
                tasks.append(task["title"])
                completed += 1
            total += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(name, completed, total))

    for t in tasks:
        print('\t {}'.format(t))
