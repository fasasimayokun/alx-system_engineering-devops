#!/usr/bin/python3
"""Using what you did in the task #0, extend your Python
script to export data in the CSV format"""

import csv
import requests
import sys


if __name__ == '__main__':
    user_ID = sys.argv[1]

    path = "https://jsonplaceholder.typicode.com/users/" + user_ID

    user_resp = requests.get(path)
    user = user_resp.json()

    username = user.get("username")

    # param = {"userId": user_ID}
    todos_resp = requests.get(path + "/todos")

    todos_dict = todos_resp.json()

    with open("{}.csv".format(user_ID), "w") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for todos in todos_dict:
            writer.writerow([user_ID, username, todos.get("completed"),
                             todos.get("title")])
