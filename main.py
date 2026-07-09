from ui.menu import show_menu
from ui.display import show_tasks
from core.tasks import add_task, get_tasks, delete_task
from rich.console import Console

console = Console()


while True:
    show_menu()

    choice = input('\nChoose an option :')

    if choice == '1':
        task = input('Enter task :')
        add_task(task)

    elif choice == '2':
        show_tasks(get_tasks())

    elif choice == '3':
        show_tasks(get_tasks())
        number = int(input('Enter task number to delete :'))
        delete_task(number - 1)

    elif choice == '4':
        console.print('[green]Exiting...[/green]')
        break

    else:
        console.print('[red]Invalid option.[/red]')




