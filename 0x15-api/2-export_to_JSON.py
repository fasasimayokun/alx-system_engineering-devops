#!/usr/bin/python3
"""Using what you did in the task #0, extend your Python
script to export data in the JSON format"""

import json
import requests
import sys


if __name__ == '__main__':
    path = "https://jsonplaceholder.typicode.com/"

    user_ID = sys.argv[1]

    user_resp = requests.get(path + "users/{}".format(user_ID))
    user = user_resp.json()
    username = user.get("username")

    data_to_expt = {user_ID: []}

    param = {"userId": user_ID}
    todos_resp = requests.get(path + "todos", params=param)
    todos_dict = todos_resp.json()

    for todos in todos_dict:
        task_info = {
                "task": todos.get("title"),
                "completed": todos.get("completed"),
                "username": username
                }
        data_to_expt[user_ID].append(task_info)

    with open("{}.json".format(user_ID), "w") as json_file:
        json.dump(data_to_expt, json_file)
