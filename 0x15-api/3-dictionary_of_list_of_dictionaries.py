#!/usr/bin/python3
"""Retrieves the TODO list for all employees.
:param user_id: The ID of the user.
"""

import json
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    """Make a GET request to the API to retrieve the employee's TODO list."""
    response = requests.get(url)
    users = response.json()

    """Parse the JSON response and extract the necessary information."""
    dictionary = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        url = url + '/todos/'
        response = requests.get(url)
        tasks = response.json()
        dictionary[user_id] = []
        for task in tasks:
            dictionary[user_id].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            })

	"""Write the completed tasks to a JSON file."""
        with open('todo_all_employees.json', 'w') as file:
        json.dump(dictionary, file)
