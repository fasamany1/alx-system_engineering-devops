#!/usr/bin/python3
"""Retrieves the TODO list progress for a given employee.
:param employeeId: The ID of the employee.
"""

import requests
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    """Make a GET request to the API to retrieve the employee's TODO list."""
    response = requests.get(url)
    username = response.json().get('username')

    """Parse the JSON response and extract the necessary information."""
    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

    """Write the completed tasks to a CSV file."""
    with open('{}.csv'.format(employeeId), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(employeeId, username, task.get('completed'),
                               task.get('title')))
