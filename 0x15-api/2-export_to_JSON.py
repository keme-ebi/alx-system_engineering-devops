#!/usr/bin/python3
"""records all tasks owned by an employee and export the data in JSON format"""

import json
import requests
import sys


if __name__ == "__main__":
    e_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"
    # get the employees username
    req = requests.get("{}/users/{}".format(url, e_id))
    data = req.json()
    username = data.get('username')

    # get full data on todos
    req = requests.get("{}/todos?userId={}".format(url, e_id))
    datas = req.json()

    filename = "{}.json".format(e_id)

    li = []

    for data in datas:
        status = data.get('completed')
        title = data.get('title')
        dic = {"task": title, "completed": status, "username": username}
        li.append(dic)

    dic1 = {e_id: li}

    with open(filename, 'w') as f:
        json.dump(dic1, f)
