from pyfiglet import figlet_format
from rich.console import Console
from rich.table import Table

console = Console()

def show_logo():
    logo = figlet_format("GRAVITAS", font="ansi_shadow")
    console.print(logo, style="white")



def show_tasks(tasks):
    table = Table(title="Tasks", show_header=True, header_style="bold green")

    table.add_column('ID')
    table.add_column('Task')

    for index, task in enumerate(tasks, start=1):
        table.add_row(str(index), task)

    console.print(table)