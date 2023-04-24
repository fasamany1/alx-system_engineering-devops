#!/usr/bin/python3

import requests

def get_employee_todo_progress(employee_id):
	"""
	Retrieves the TODO list progress for a given employee ID.
	:param employee_id: The ID of the employee.
	"""

        """ Make a GET request to the API to retrieve the employee's TODO list."""
	response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")

	""" Parse the JSON response and extract the necessary information."""
	todos = response.json()
	employee_name = todos[0]['name']
	total_tasks = len(todos)
	done_tasks = sum(1 for todo in todos if todo['completed'])
	completed_tasks = [todo['title'] for todo in todos if todo['completed']]

	""" Print out the results in the required format."""
	print(f"Employee {employee_name} is done with tasks ({done_tasks}/{total_tasks}):")
	for task in completed_tasks:
		print(f"\t- {task}")

if __name__ == "__main__":
	""" Call the function with the provided employee ID."""
	get_employee_todo_progress(1)
