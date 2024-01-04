#!/usr/bin/python3
"""records all tasks owned by an employee and export the data in CSV format"""

import csv
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

    filename = "{}.csv".format(e_id)

    with open(filename, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)

        for data in datas:
            user_id = data.get('userId')
            status = data.get('completed')
            title = data.get('title')
            writer.writerow([user_id, username, status, title])
