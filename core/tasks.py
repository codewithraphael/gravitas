from core.storage import load_tasks, save_tasks

tasks = load_tasks()

def add_task(task):
    tasks.append(task)
    save_tasks(tasks)
    print(f'Task "{task}" added successfully')


def get_tasks():
   return tasks


def delete_task(number):
    tasks.pop(number - 1)
    save_tasks(tasks)
    print('Task deleted successfully')