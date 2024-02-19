#!/usr/bin/python3
"""Using what you did in the task #0, extend your Python
script to export data in the JSON format"""

import json
import requests
import sys


if __name__ == '__main__':
    user_ID = sys.argv[1]

    path = "https://jsonplaceholder.typicode.com/users/" + user_ID

    user_resp = requests.get(path)
    user = user_resp.json()
    username = user.get("username")

    data_to_expt = {user_ID: []}

    # param = {"userId": user_ID}
    todos_resp = requests.get(path + "/todos")
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
