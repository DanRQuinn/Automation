import os
import shutil
from rich.console import Console
from rich.prompt import Prompt

console = Console()
prompt = Prompt()

def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        console.print(f"Folder {folder_name} created successfully", style="bold green")
    else:
        console.print(f"Folder {folder_name} already exists", style="bold red")

if __name__ == "__main__":
    folder_name = prompt.ask("What is the name of the folder?")
    create_folder(folder_name)
