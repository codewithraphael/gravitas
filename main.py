from ui.menu import show_menu
from ui.display import show_tasks
from core.tasks import add_task, get_tasks, delete_task


while True:
    show_menu()

    choice = input('\nChoose an option :')

    if choice == '1':
        task = input('Enter task :')
        add_task(task)
        print(f'Task "{task}" added successfully')

    elif choice == '2':
        show_tasks(get_tasks())

    elif choice == '3':
        show_tasks(get_tasks())
        number = int(input('Enter task number to delete :'))
        delete_task(number - 1)

    elif choice == '4':
        break

    else:
        print('Invalid option.')




