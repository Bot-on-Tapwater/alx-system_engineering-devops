#!/usr/bin/python3

"""Gather data from an API"""

if __name__ == '__main__':
    import requests
    import sys
    import urllib

    # grab id from cmd args
    employee_id = sys.argv[1]

    # api url
    user_api_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_api_url = f'https://jsonplaceholder.typicode.com/todos'
    params = {'userId': employee_id}

    # use requests to fetch data from url
    employee_details = requests.get(user_api_url)

    emp_name = employee_details.json()['name']

    total_todos = requests.get(todos_api_url, params)

    cmpl_tds = []

    for todo in total_todos.json():
        if todo['completed'] is True:
            cmpl_tds.append(todo)

    task_completion_ratio = f'({len(cmpl_tds)}/{len(total_todos.json())})'

    print(f'Employee {emp_name} is done with tasks{task_completion_ratio}:')

    for todo in cmpl_tds:
        print(f'\t {todo["title"]}')
