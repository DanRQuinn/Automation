from rich.console import Console
from rich.prompt import Prompt
import os
import shutil

console = Console()
prompt = Prompt()

def move_user_documents(folder, file):
    os.makedirs("temp", exist_ok=True)
    shutil.move(f"{folder}/{file}", "temp")

if __name__ == "__main__":
    folder = prompt.ask("What is the name of the folder?")
    file = prompt.ask("What is the name of the file?")
    if os.path.exists(f"{folder}/{file}"):
      move_user_documents(folder, file)
      console.print(f"Moved {file} from {folder} to temp", style="bold green")
    else:
      console.print(f"{folder}/{file} does not exist", style="bold red")

