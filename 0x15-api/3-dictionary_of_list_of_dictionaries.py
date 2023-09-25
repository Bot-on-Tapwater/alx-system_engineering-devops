#!/usr/bin/python3

"""Export to JSON"""

if __name__ == '__main__':
    import csv
    import json
    import requests
    import sys
    import urllib

    # api url
    user_api_url = f'https://jsonplaceholder.typicode.com/users/'
    todos_api_url = f'https://jsonplaceholder.typicode.com/todos'

    # use requests to fetch data from url
    # employee_details = requests.get(user_api_url)

    # emp_name = employee_details.json()['username']

    # all tasks done by all users
    total_todos = requests.get(todos_api_url)

    # all users
    all_users = requests.get(user_api_url)

    # dict containing emp_id: emp_tasks key value pair
    all_tasks = {}

    # list containing emp_tasks
    all_tds = []

    # name of json file
    json_file = f'todo_all_employees.json'

    # open file in write mode
    with open(json_file, mode="w") as file:

        # loop through all users grabbing id and username
        for user in all_users.json():
            emp_id = user['id']
            emp_name = user['username']

            params = {'userId': emp_id}

            # all tasks done by all users
            total_todos = requests.get(todos_api_url, params)

            for todo in total_todos.json():
                cmpl = todo['completed']
                ttl = todo['title']
                all_tds.append(
                    {"username": emp_name, "task": ttl, "completed": cmpl})

            # data = {f"{emp_id}": all_tds}
            all_tasks[f"{emp_id}"] = all_tds
            all_tds = []

        json.dump(all_tasks, file)
