#!/usr/bin/python3
"""returns information about an employees todo list progress"""

import json
import requests
import sys


if __name__ == "__main__":
    e_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"
    # get the employees name
    req = requests.get("{}/users/{}".format(url, e_id))
    data = req.json()
    name = data.get('name')

    # get the number of tasks done and total number of tasks
    req = requests.get("{}/todos?userId={}".format(url, e_id))
    data = req.json()
    total = len(data)
    t_done = sum(tasks['completed'] for tasks in data)

    print("Employee {} is done with tasks({}/{}):".format(name, t_done, total))
    for tasks in data:
        if tasks['completed']:
            print("\t {}".format(tasks.get('title')))
