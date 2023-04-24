#!/usr/bin/python3
"""Retrieves the TODO list progress for a given employee ID.
:param employeeId: The ID of the employee.
"""

import requests
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    """ Make a GET request to the API to retrieve the employee's TODO list."""
    response = requests.get(url)
    employeeName = response.json().get('name')

    """Parse the JSON response and extract the necessary information."""
    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()
    done = 0
    done_tasks = []

    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employeeName, done, len(tasks)))

    """Print out the results in the required format."""
    for task in done_tasks:
        print("\t {}".format(task.get('title')))
