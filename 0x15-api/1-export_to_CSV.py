#!/usr/bin/python3
"""
this module gets information about an employee and exports it to a csv file
"""
import csv
import requests
import sys


if __name__ == '__main__':
    arg = sys.argv[1]
    csv_file = "{}.csv".format(arg)
    # general url
    url = 'https://jsonplaceholder.typicode.com'
    # url leading to the users with arg as parameter
    first_req = requests.get("{}/users/{}".format(url, arg))
    # url leading to todos of users
    second_req = requests.get("{}/todos?userId={}".format(url, arg))
    # convert first request to json format
    user = first_req.json()
    # get the name of the employee/user identified by the id passed as arg
    username = user.get('username')
    # convert second request to json format
    tasks = second_req.json()
    data = []

    # get each title where completed or not
    for task in tasks:
        # get each records needed
        user_id = task.get('userId')
        complete_stat = task.get('completed')
        title = task.get('title')
        data.append([user_id, username, complete_stat, title])

    # export data to a csv file
    with open(csv_file, mode='w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(data)
