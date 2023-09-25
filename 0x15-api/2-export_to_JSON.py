#!/usr/bin/python3

"""Export to JSON"""

if __name__ == '__main__':
    import csv
    import json
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

    all_tds = []

    json_file = f'{employee_id}.json'

    with open(json_file, mode="w") as file:

        for todo in total_todos.json():
            cmpl = todo['completed']
            ttl = todo['title']
            all_tds.append(
                {"task": ttl, "completed": cmpl, "username": emp_name})

        data = {f"{employee_id}": all_tds}
        json.dump(data, file)
