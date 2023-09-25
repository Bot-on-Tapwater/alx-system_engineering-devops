#!/usr/bin/python3

"""Export to CSV"""

if __name__ == '__main__':
    import csv
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

    emp_name = employee_details.json()['username']

    total_todos = requests.get(todos_api_url, params)

    cmpl_tds = []

    for todo in total_todos.json():
        if todo['completed'] is True:
            cmpl_tds.append(todo)

    csv_file = f'{employee_id}.csv'

    with open(csv_file, mode="w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in total_todos.json():
            cmpl = todo['completed']
            ttl = todo['title']
            writer.writerow([employee_id, emp_name, cmpl, ttl])

    task_completion_ratio = f'({len(cmpl_tds)}/{len(total_todos.json())})'
