#!/usr/bin/python3
""" Module for save_tasks_to_json function """

import json
import requests
import sys


def save_tasks_to_json(employeeId):
    """ Using a REST API, for a given employee ID, returns info about
    his/her TODO list progress
    """

    username = ''
    userDict = {}

    usersRes = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(employeeId))
    todosRes = requests.get('https://jsonplaceholder.typicode.com/users/{}/'
                            'todos'.format(employeeId))
    username = usersRes.json().get('username')
    todosJson = todosRes.json()
    userDict[employeeId] = []

    for task in todosJson:
        taskDict = {}
        taskDict['task'] = task.get('title')
        taskDict['username'] = username
        taskDict['completed'] = task.get('completed')
        userDict[employeeId].append(taskDict)

    with open('{}.json'.format(employeeId), 'w') as jsonFile:
        json.dump(userDict, jsonFile)

    return 0

if __name__ == "__main__":
    save_tasks_to_json(sys.argv[1])
