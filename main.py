# gravitas cli To-do list app  v 1.0.0

def show_menu():
    print('='*100)
    print(f"GRAVITAS : /'gravItas/ noun: ability to remain calm, composed & respected under pressure")
    print('='*100)
    print('[1.] Add Task')
    print('[2.] View Task')
    print('[3.] Delete Task')
    print('[4.] Exit')

tasks = []

while True:
    show_menu()

    choice = input('\nChoose an option :')

    if choice == '1':
        task = input('Enter task :')
        tasks.append(task)
        print(f'Task "{task}" added successfully')

    elif choice == '2':
        print('='*10)
        print('Tasks')
        print('='*10)

        for index, task in enumerate(tasks):
            print(f'{index + 1}. {task}')

    elif choice == '3':
        number = int(input('Enter task number to delete :'))
        tasks.pop(number - 1)
        print('Task deleted successfully')

    elif choice == '4':
        break

