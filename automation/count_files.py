from rich.console import Console
from rich.prompt import Prompt
import os
import shutil

console = Console()
prompt = Prompt()

def count(file_extention, folder_path):
    files = os.listdir(folder_path)
    count = 0
    for file in os.listdir(folder_path):
        file = os.path.join(folder_path, file)
        if file.endswith(file_extention):
            count += 1
    console.print(f"There are {count} {file_extention} files in {folder_path}", style="bold green")

if __name__ == "__main__":
    file_extention = prompt.ask("What file extention do you want to count?")
    folder_path = prompt.ask("What folder do you want to search?")
    if os.path.exists(folder_path):
        console.print(f"Number of {file_extention} files in {folder_path}", style="bold green")
    else:
        console.print(f"{folder_path} does not exist", style="bold red")
