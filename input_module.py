import json

def load_tasks(file_path='tasks.json'):
    with open(file_path, 'r') as f:
        tasks = json.load(f)
    return tasks
