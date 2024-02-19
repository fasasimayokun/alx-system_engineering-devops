#!/usr/bin/python3
"""a script that, using this REST API, for a given employee ID
returns information about his/her TODO list progress"""

import requests
import sys


if __name__ == '__main__':
    endpoints = "https://jsonplaceholder.typicode.com/"

    employee_ID = sys.argv[1]

    user_resp = requests.get(endpoints + "users/{}".format(employee_ID))
    user = user_resp.json()
    param = {"userId": employee_ID}

    todos_resp = requests.get(endpoints + "todos", params=param)
    todos_dict = todos_resp.json()

    completed = []

    for todos in todos_dict:
        if todos.get("completed") is True:
            completed.append(todos.get("title"))

    print("Employee {} is done with tasks({}/{})".format(user.get("name"),
                                                       len(completed),
                                                       len(todos_dict)))
    for complete in completed:
        print("\t {}".format(complete))
