#!/usr/bin/python3
"""Retrieves the TODO list for all employees."""

import json
import requests

def get_tasks_from_employee(response, employee):
	"""Get all the tasks of an employee
	Creates a list to stores all the tasks of the employee
	"""
        employee_tasks = list()

	for task in response:
		if task.get('userId') == employee.get('id'):
			task_data = {
				'username': employee.get('username'),
				'task': task.get('title'),
				'completed': task.get('completed'),
			}

			employee_tasks.append(task_data)

	return employee_tasks

if __name__ == '__main__':
	""" Formatted names of API urls and filenames"""
	api_url = 'https://jsonplaceholder.typicode.com'
	users_uri = '{api}/users'.format(api=api_url)
	todos_uri = '{api}/todos'.format(api=api_url)
	filename = 'todo_all_employees.json'

	u_res = requests.get(users_uri).json()
	t_res = requests.get(todos_uri).json()
	users_tasks = dict()

	"""Store tasks of employee in the API data"""
	for user in u_res:
		user_id = user.get('id')

		"""current employee tasks"""
		user_tasks = get_tasks_from_employee(t_res, {
			'id': user_id,
			'username': user.get('username')
		})

		"""Insert a liist of all employee tasks in a dictionary"""
		users_tasks[user_id] = user_tasks

	"""Create a new file with employees information"""
	with open(filename, 'w', encoding='utf-8') as jsonfile:
		jsonfile.write(dumps(users_tasks))
