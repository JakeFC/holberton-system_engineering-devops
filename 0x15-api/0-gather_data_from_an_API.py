#!/usr/bin/python3
""" Module for get_employee_tasks function """

import requests
import sys


def get_employee_tasks(employeeId):
    """ Using a REST API, for a given employee ID, returns info about
    his/her TODO list progress
    """

    name = ''
    task_list = []
    completed_counter = 0

    usersRes = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(employeeId))
    todosRes = requests.get('https://jsonplaceholder.typicode.com/users/{}/\
                            todos'.format(employeeId))

    # print('usersRes: {}\n'.format(usersRes))
    # print('todosRes: {}\n'.format(todosRes))

    name = usersRes.json().get('name')
    print("name: {}".format(name))

    todosJson = todosRes.json()

    for task in todosJson:
        if task.get('completed'):
            completed_counter += 1
            task_list.append(task.get('title'))
    print('task_list: {}'.format(task_list))
    print('Employee {} is done with tasks({}/{}):'.format(name,
          completed_counter, len(todosJson)))

    for title in task_list:
        print("\t {}".format(title))

    return 0

if __name__ == "__main__":
    get_employee_tasks(sys.argv[1])
