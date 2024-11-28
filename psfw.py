# This is an enhanced version of Mini
import os
import time
from datetime import datetime

LOGO = """PressyOS Mini FWork"""
version = "FWork"

GREEN, BLUE, RESET, RED = "\033[1;32m", "\033[1;34m", "\033[0m", "\033[1;31m"

class PressyOSMiniFWork:
    def __init__(self):
        self.version = version
        self.curr_dir = os.getcwd()

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
                cmd = input(f"{BLUE}PressyMiniFWork > {RESET}").strip().lower()
                actions = {
                    "help": self.help, "date": self.show_date, 
                    "mkdir": self.mkdir, "rmdir": self.rmdir, 
                    "touch": self.touch, "ls": self.ls, "clear": self.clear, 
                    "calc": self.calc, "cd": self.cd, 
                    "cat": self.cat, "del": self.del_file
                }
                try:
                    actions.get(cmd, self.invalid)()
                except Exception as e:
                    print(f"{RED}Error during command execution: {e}{RESET}")
        except Exception as e:
            print(f"{RED}Fatal error in run loop: {e}{RESET}")

    def invalid(self): 
        print(f"{GREEN}PressyOS Mini FWork says: 'Oops! Command not found. Type 'help' for help.'{RESET}")

    def help(self):
        print(f"{GREEN}PressyOS Mini FWork Help - Available Commands:{RESET}")
        print(f"{GREEN}1. date - Check current time.\n2. mkdir - Create a directory.\n3. rmdir - Remove a directory.")
        print(f"4. touch - Create a file.\n5. ls - List directory contents.\n6. clear - Clear terminal screen.")
        print(f"7. calc - Simple calculator.\n8. cd - Change directory.\n9. cat - Show file contents.\n10. del - Delete a file.{RESET}")

    def show_date(self):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{GREEN}Current Date/Time: {current_time}{RESET}")

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
    pressy_fwork = PressyOSMiniFWork()
    pressy_fwork.run()