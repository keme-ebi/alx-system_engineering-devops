#!/usr/bin/python3
"""
this module gets information about all employee and exports it to a json file
"""
import json
import requests


if __name__ == '__main__':
    json_file = "todo_all_employees.json"
    # general url
    url = 'https://jsonplaceholder.typicode.com'
    # url leading to the users with arg as parameter
    first_req = requests.get("{}/users".format(url))
    # convert first request to json format
    users = first_req.json()
    # create a dictionary to store all data
    dic = {}
    # get the name of the employee/user identified by the id passed as arg
    for user in users:
        username = user.get('username')
        user_id = user.get('id')
        # get url leading to todos using the id gotten from 1st url
        second_req = requests.get("{}/todos?userId={}".format(url, user_id))
        # convert second request to json
        tasks = second_req.json()
        data = []
        # get each title where completed or not
        for task in tasks:
            # get each records needed
            user_id = task.get('userId')
            complete_stat = task.get('completed')
            title = task.get('title')
            data.append({'task': title,
                         'completed': complete_stat,
                         'username': username, })

        dic[user_id] = data

    # export data to a json file
    with open(json_file, mode='w') as file:
        json.dump(dic, file)
