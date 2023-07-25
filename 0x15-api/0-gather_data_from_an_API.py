#!/usr/bin/python3
"""
this module returns information about an employee
"""
import requests
import sys


if __name__ == '__main__':
    arg = sys.argv[1]
    # general url
    url = 'https://jsonplaceholder.typicode.com'
    # url leading to the users with arg as parameter
    first_req = requests.get("{}/users/{}".format(url, arg))
    # url leading to todos of users
    second_req = requests.get("{}/todos?userId={}".format(url, arg))
    # convert first request to json format
    employee = first_req.json()
    # get the name of the employee/user identified by the id passed as arg
    employee = employee.get('name')
    # convert second request to json format
    tasks = second_req.json()
    titles = []

    # get each title where completed or not
    for task in tasks:
        # sort out and get only tasks that are completed
        if task.get('completed') is True:
            # add the title of each completed tasks to the list
            titles.append(task.get('title'))

    # string that prints employee name and number of completed tasks/general
    print("Employee {} is done with tasks({}/{}):".format(
        employee, len(titles), len(tasks)))

    # print out the title of completed tasks from the list
    for t in titles:
        print("\t {}".format(t))
