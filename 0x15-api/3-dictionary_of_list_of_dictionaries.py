#!/usr/bin/python3
"""Using what you did in the task #0, extend your Python
script to export data in the JSON format"""

import json
import requests


if __name__ == '__main__':
    path = "https://jsonplaceholder.typicode.com/"

    users = requests.get(path + "users").json()
    # username = users.get("username")

    data_to_expt = {}

    for user in users:
        user_ID = user.get("id")

        todos_resp = requests.get(path + "todos?userId={}".format(user_ID))
        todos_dict = todos_resp.json()

        data_to_expt[user_ID] = []

        for todos in todos_dict:
            task_info = {
                    "task": todos.get("title"),
                    "completed": todos.get("completed"),
                    "username": user.get("username")
                }
            data_to_expt[user_ID].append(task_info)

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(data_to_expt, json_file)
