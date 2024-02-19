#!/usr/bin/python3
"""Using what you did in the task #0, extend your Python
script to export data in the CSV format"""

import csv
import requests
import sys


if __name__ == '__main__':
    path = "https://jsonplaceholder.typicode.com/"

    user_ID = sys.argv[1]

    user_resp = requests.get(path + "users/{}".format(user_ID))
    user = user_resp.json()

    username = user.get("username")

    param = {"userId": user_ID}
    todos_resp = requests.get(path + "todos", params=param)

    todos_dict = todos_resp.json()

    with open("{}.csv".format(user_ID), "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for todos in todos_dict:
            writer.writerow([user_ID, username, todos.get("completed"),
                             todos.get("title")])
