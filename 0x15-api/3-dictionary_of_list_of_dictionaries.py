#!/usr/bin/python3
"""records all tasks from all employees and export the data in JSON format"""

import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    # get the employees username
    req = requests.get("{}/users".format(url))
    all_employees = req.json()
    dic1 = {}

    for employee in all_employees:
        e_id = employee.get('id')
        username = employee.get('username')
        # get full data on todos
        todo_req = requests.get("{}/todos?userId={}".format(url, e_id))
        datas = todo_req.json()

        li = []
        for data in datas:
            status = data.get('completed')
            title = data.get('title')
            dic = {"task": title, "completed": status, "username": username}
            li.append(dic)

        dic1[e_id] = li

    filename = "todo_all_employees.json"
    with open(filename, 'w') as f:
        json.dump(dic1, f)
