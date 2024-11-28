import os
import time
from datetime import datetime
import random

LOGO = """PressyOS Mini"""
version = "Mini"

GREEN, BLUE, RESET, RED = "\033[1;32m", "\033[1;34m", "\033[0m", "\033[1;31m"

class PressyOSMini:
    def __init__(self):
        self.version = version
        self.curr_dir = os.getcwd()
        self.todo_data = []

    def type_effect(self, text, speed=0.05): 
        for char in text: 
            print(char, end='', flush=True)
            time.sleep(speed)
        print()

    def run(self):
        try:
            self.type_effect(f"{BLUE}Initializing...{RESET}", speed=0.00001)
            time.sleep(0.5); os.system('cls' if os.name == 'nt' else 'clear')  
            self.type_effect(f"{GREEN}{LOGO} v{self.version}{RESET}", speed=0.001)
            while True:
                cmd = input(f"{BLUE}PressyMini > {RESET}").strip().lower()
                actions = {
                    "help": self.help, "todo": self.todo, "date": self.show_date, 
                    "joke": self.joke, "mkdir": self.mkdir, "rmdir": self.rmdir, 
                    "touch": self.touch, "ls": self.ls, "clear": self.clear, 
                    "calc": self.calc, "task": self.task, "cd": self.cd, 
                    "cat": self.cat, "del": self.del_file
                }
                try:
                    actions.get(cmd, self.invalid)()
                except Exception as e:
                    print(f"{RED}Error during command execution: {e}{RESET}")
        except Exception as e:
            print(f"{RED}Fatal error in run loop: {e}{RESET}")

    def invalid(self): 
        print(f"{GREEN}PressyOS Mini says: 'Oops! Command not found. Type 'help' for help.'{RESET}")

    def help(self):
        print(f"{GREEN}PressyOS Mini Help - Available Commands:{RESET}")
        print(f"{GREEN}1. todo - Manage tasks.\n2. date - Check current time.\n3. joke - Get a joke.\n4. mkdir - Create a directory.\n5. rmdir - Remove a directory.")
        print(f"6. touch - Create a file.\n7. ls - List directory contents.\n8. clear - Clear terminal screen.\n9. calc - Simple calculator.")
        print(f"10. task - Show active processes.\n11. cd - Change directory.\n12. cat - Show file contents.\n13. del - Delete a file.{RESET}")

    def show_date(self):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{GREEN}Current Date/Time: {current_time}{RESET}")

    def joke(self):
        joke = random.choice([
            "Why don't skeletons fight each other? They don't have the guts!",
            "I told my computer I needed a break... It froze.",
            "Why did the developer go broke? Because he used up all his cache!"
        ])
        print(f"{GREEN}PressyMini’s Joke: {joke}{RESET}")

    def todo(self):
        while True:
            action = input(f"{BLUE}To-do > {RESET}").strip().lower()
            if action == "add": 
                self.todo_data.append(input(f"{BLUE}Enter task: {RESET}"))
            elif action == "remove":
                task = input(f"{BLUE}Enter task to remove: {RESET}")
                if task in self.todo_data: 
                    self.todo_data.remove(task)
                    print(f"{GREEN}Task removed.{RESET}")
                else: 
                    print(f"{GREEN}Task not found.{RESET}")
            elif action == "show": 
                print(f"{GREEN}Your to-do list: {RESET}")
                for task in self.todo_data: 
                    print(f"{GREEN}- {task}{RESET}")
            elif action == "exit": break

    def mkdir(self):
        dir_name = input(f"{BLUE}Enter directory name: {RESET}")
        try:
            os.makedirs(dir_name, exist_ok=True)
            print(f"{GREEN}Directory '{dir_name}' created.{RESET}")
        except Exception as e:
            print(f"{RED}Error: {e}{RESET}")

    def rmdir(self):
        dir_name = input(f"{BLUE}Enter directory to remove: {RESET}")
        try:
            os.rmdir(dir_name)
            print(f"{GREEN}Directory '{dir_name}' removed.{RESET}")
        except Exception as e:
            print(f"{RED}Error: {e}{RESET}")

    def touch(self):
        file_name = input(f"{BLUE}Enter file name: {RESET}")
        try:
            open(file_name, 'w').close()
            print(f"{GREEN}File '{file_name}' created.{RESET}")
        except Exception as e:
            print(f"{RED}Error: {e}{RESET}")

    def ls(self):
        print(f"{GREEN}Directory contents in '{self.curr_dir}':{RESET}")
        for item in os.listdir(self.curr_dir):
            print(f"{GREEN}- {item}{RESET}")

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def calc(self):
        while True:
            expression = input(f"{BLUE}Calc > {RESET}").strip()
            if expression == "exit": break
            try: 
                print(f"{GREEN}Result: {eval(expression)}{RESET}")
            except Exception as e: 
                print(f"{RED}Error: {e}{RESET}")

    def task(self): 
        print(f"{GREEN}PressyOS Mini Task: No active processes in this simulation.{RESET}")

    def cd(self):
        new_dir = input(f"{BLUE}Enter directory to change to: {RESET}")
        try:
            os.chdir(new_dir)
            self.curr_dir = os.getcwd()
            print(f"{GREEN}Changed directory to {self.curr_dir}{RESET}")
        except Exception as e:
            print(f"{RED}Error: {e}{RESET}")

    def cat(self):
        file_name = input(f"{BLUE}Enter file name to view: {RESET}")
        try:
            with open(file_name, 'r') as file:
                print(f"{GREEN}Contents of {file_name}:\n{RESET}{file.read()}")
        except Exception as e:
            print(f"{RED}Error: {e}{RESET}")

    def del_file(self):
        file_name = input(f"{BLUE}Enter file name to delete: {RESET}")
        try:
            os.remove(file_name)
            print(f"{GREEN}File '{file_name}' deleted.{RESET}")
        except Exception as e:
            print(f"{RED}Error: {e}{RESET}")

if __name__ == "__main__":
    pressy = PressyOSMini()
    pressy.run()