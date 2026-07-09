def show_tasks(tasks):
    print('='*10)
    print('Tasks')
    print('='*10)

    for index, task in enumerate(tasks, start=1):
        print(f'{index}. {task}')