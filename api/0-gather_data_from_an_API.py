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
    task_title = []
    url_user = "https://jsonplaceholder.typicode.com/users/" + id
    user = requests.get(url_user).json()
    name = user.get("name")
    todos = "https://jsonplaceholder.typicode.com/todos/"
    task_list = requests.get(todos).json()
    for t in task_list:
        if t.get("userId") == int(id):
            if t.get("completed") is True:
                task_title.append(t["title"])
                completed += 1
            total += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(name, completed, total))
    for y in task_title:
        print("\t {}".format(y))
