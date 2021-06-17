#!/usr/bin/python3
"""Save all info to a JSON file"""

import json
import requests


def save_all_to_json():
    """
    Save info to a JSON file. That info? Still employee record.
    """

    users_and_tasks = {}

    users_json = requests.get('https://jsonplaceholder.typicode.com/users')\
        .json()
    todos_json = requests.get('https://jsonplaceholder.typicode.com/todos')\
        .json()

    user_info = {}
    for user in users_json:
        user_info[user['id']] = user['username']

    for task in todos_json:
        if users_and_tasks.get(task['userId'], False) is False:
            users_and_tasks[task['userId']] = []
        task_dict = {}
        task_dict['username'] = user_info[task['userId']]
        task_dict['task'] = task['title']
        task_dict['completed'] = task['completed']
        users_and_tasks[task['userId']].append(task_dict)

    with open('todo_all_employees.json', 'w') as jsonFile:
        json.dump(users_and_tasks, jsonFile)

    return 0

if __name__ == "__main__":
    save_all_to_json()
