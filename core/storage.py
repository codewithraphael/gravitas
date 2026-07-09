def load_tasks():
    try:
        with open('tasks.txt') as file:
            tasks = file.read().splitlines()
            return tasks
    except FileNotFoundError:
        return []
    

def save_tasks(tasks):
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(task + '\n')