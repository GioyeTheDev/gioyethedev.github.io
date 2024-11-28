import os
import time
import random
import sys
from datetime import datetime
import requests

LOGO = """ ______                            _______ ______ 
(_____ \\                          (_______) _____)
 _____) )___ _____  ___  ___ _   _ _     ( (____  
|  ____/ ___) ___ |/___)/___) | | | |   | \\____ \\ 
| |   | |   | ____|___ |___ | |_| | |___| |____) )
|_|   |_|   |_____|___/(___/ \\__  |\\_____(______/ 
                            (____/                """
MASCOT = """    (0-0)
    /[_]​\\
     | |  """
GREEN, BLUE, YELLOW, RED, PURPLE, RESET = "\033[1;32m", "\033[1;34m", "\033[1;33m", "\033[1;31m", "\033[1;35m", "\033[0m"
COLORS = [GREEN, BLUE, YELLOW, RED, PURPLE]

class PressyOS:
    def __init__(self):
        self.notes_data, self.todo_data = {}, []
        self.version, self.curr_dir = "1.0.1", os.getcwd()

    def type_effect(self, text, speed=0.05): 
        for char in text: 
            print(char, end='', flush=True)
            time.sleep(speed)
        print()

    def run(self):
        try:
            self.type_effect(f"{BLUE}Initializing...{RESET}", speed=0.00001)
            time.sleep(0.5); os.system('cls' if os.name == 'nt' else 'clear')  
            self.type_effect(f"{GREEN}{LOGO}{RESET}", speed=0.001)
            print(f"{GREEN}PressyOS v{self.version}{RESET}\n{GREEN}{MASCOT}{RESET}\n{GREEN}Welcome to PressyOS! Type HELP For Commands.{RESET}")
            while True:
                cmd = input(f"{BLUE}Pressy > {RESET}").strip().lower()
                actions = {
                    "help": self.help, "todo": self.todo, "notes": self.notes,
                    "calc": self.calc, "task": self.task, "date": self.show_date, 
                    "joke": self.joke, "remind": self.remind, "mkdir": self.mkdir, 
                    "rmdir": self.rmdir, "touch": self.touch, "cat": self.cat, 
                    "ls": self.ls, "del": self.del_file, "clear": self.clear,
                    
                }
                try:
                    actions.get(cmd, self.invalid)()
                except Exception as e:
                    print(f"{RED}Error during command execution: {e}{RESET}")
        except Exception as e:
            print(f"{RED}Fatal error in run loop: {e}{RESET}")

    def invalid(self): 
        print(f"{GREEN}Pressy says: 'Oops! Command not found. Type 'help' for help.'{RESET}")

    def help(self):
        print(f"{GREEN}PressyOS Help - Available Commands:{RESET}\n{GREEN}1. todo - Manage tasks.\n2. notes - Manage notes.\n3. calc - Simple math.\n4. task - System processes.\n5. date - Check current time.\n6. joke - Get a joke.\n7. remind - Set reminders.\n8. mkdir - Create a directory.\n9. rmdir - Remove a directory.\n10. touch - Create a file.\n11. cat - Show file contents.\n12. ls - List directory contents.\n13. del - Delete a file.\n14. clear - Clear terminal screen.{RESET}")

    def todo(self):
        while True:
            action = input(f"{BLUE}To-do > {RESET}").strip().lower()
            if action == "add": self.todo_data.append(input(f"{BLUE}Enter task: {RESET}"))
            elif action == "remove":
                task = input(f"{BLUE}Enter task to remove: {RESET}")
                if task in self.todo_data: 
                    self.todo_data.remove(task); print(f"{GREEN}Task removed.{RESET}")
                else: print(f"{GREEN}Task not found.{RESET}")
            elif action == "show": 
                print(f"{GREEN}Your to-do list: {RESET}")
                for task in self.todo_data: print(f"{GREEN}- {task}{RESET}")
            elif action == "exit": break

    def notes(self):
        while True:
            action = input(f"{BLUE}Notes > {RESET}").strip().lower()
            if action == "add":
                note = input(f"{BLUE}Enter note: {RESET}")
                title = input(f"{BLUE}Enter title: {RESET}")
                self.notes_data[title] = note
                print(f"{GREEN}Note saved!{RESET}")
            elif action == "show":
                if not self.notes_data: print(f"{GREEN}No notes available.{RESET}")
                for title, note in self.notes_data.items(): print(f"{GREEN}Title: {title}\nNote: {note}{RESET}")
            elif action == "remove":
                title = input(f"{BLUE}Enter title to remove: {RESET}")
                if title in self.notes_data: del self.notes_data[title]; print(f"{GREEN}Note removed.{RESET}")
                else: print(f"{GREEN}Note not found.{RESET}")
            elif action == "exit": break

    def calc(self):
        while True:
            expression = input(f"{BLUE}Calc > {RESET}").strip()
            if expression == "exit": break
            try: print(f"{GREEN}Result: {eval(expression)}{RESET}")
            except Exception as e: print(f"{RED}Error: {e}{RESET}")

    def task(self): 
        print(f"{GREEN}PressyOS Task: No active processes in this simulation.{RESET}")

    def show_date(self):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{GREEN}Current Date/Time: {current_time}{RESET}")

    def joke(self):
        joke = random.choice([
            "Why don't skeletons fight each other? They don't have the guts!",
            "I told my computer I needed a break... It froze.",
            "Why did the developer go broke? Because he used up all his cache!",
            "I tried to start a band called 1023MB, but we never got a gig."
        ])
        print(f"{GREEN}Pressy’s Joke: {joke}{RESET}")

    def remind(self):
        reminder = input(f"{BLUE}Enter reminder: {RESET}")
        time_in = input(f"{BLUE}In how many minutes? {RESET}")
        try:
            time_in = int(time_in)
            print(f"{GREEN}Reminder set! I will remind you in {time_in} minutes.{RESET}")
            time.sleep(time_in * 60)
            print(f"{GREEN}Reminder: {reminder}{RESET}")
        except ValueError:
            print(f"{RED}Invalid time format.{RESET}")

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

    def cat(self):
        file_name = input(f"{BLUE}Enter file name to view: {RESET}")
        try:
            with open(file_name, 'r') as file:
                print(f"{GREEN}Meow! I mean:\n{RESET}{file.read()}")
        except Exception as e:
            print(f"{RED}Error: {e}{RESET}")

    def ls(self):
        print(f"{GREEN}Directory contents:{RESET}")
        for item in os.listdir(self.curr_dir):
            print(f"{GREEN}- {item}{RESET}")

    def del_file(self):
        file_name = input(f"{BLUE}Enter file name to delete: {RESET}")
        try:
            os.remove(file_name)
            print(f"{GREEN}File '{file_name}' deleted.{RESET}")
        except Exception as e:
            print(f"{RED}Error: {e}{RESET}")

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

# import requests

def telehack(self):
    url = "https://telehack.com"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        print(f"{GREEN}Telehack Website Content:{RESET}")
        print(response.text[:1000])  # Display the first 1000 characters (to avoid printing too much)
        input(f"{BLUE}Press Enter to return to the command line.{RESET}")
    except requests.exceptions.RequestException as e:
        print(f"{RED}Error fetching Telehack content: {e}{RESET}")
        input(f"{BLUE}Press Enter to return to the command line.{RESET}")

if __name__ == "__main__":
    pressy = PressyOS()
    pressy.run()