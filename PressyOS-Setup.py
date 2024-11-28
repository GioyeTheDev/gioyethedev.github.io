import os
import time
import requests
from datetime import datetime


class PressyOSSetup:
    def __init__(self):
        self.collection = {
            "1.0.0": "PressyOS 1.0.0",
            "1.0.1": "PressyOS 1.0.1",
            "Mini": "PressyOS Mini",
            "Mini FWork": "PressyOS Mini FWork",
            "HTML": "PressyOS Mini HTML",  # Now below Mini
            "Micro": "PressyOS Micro",
            "Nano": "PressyOS Nano",
        }
        self.urls = {
            "1.0.0": "https://gioyethedev.github.io/ps.py",
            "1.0.1": "https://gioyethedev.github.io/ps1.py",
            "Mini": "https://gioyethedev.github.io/psm.py",
            "Mini FWork": "https://gioyethedev.github.io/psfw.py",
            "HTML": "https://files.catbox.moe/qz12zs.py",  # URL for PressyOS Mini HTML
        }
        self.rainbow_colors = [
            "\033[41m",  # Red
            "\033[43m",  # Yellow
            "\033[42m",  # Green
            "\033[46m",  # Cyan
            "\033[44m",  # Blue
            "\033[45m",  # Magenta
        ]

    def type_text(self, text, end="\n"):
        """Simulate typing effect for displaying text."""
        for char in text:
            print(char, end="", flush=True)
            time.sleep(0.001)
        if end:
            print(end, end="", flush=True)

    def display_clock(self):
        """Display the current time in the format: HH:MM:SS."""
        current_time = datetime.now().strftime("%H:%M:%S")
        self.type_text(f"\033[36m[Time: {current_time}] \033[0m", end="")

    def display_header(self):
        """Display the setup header."""
        os.system("cls" if os.name == "nt" else "clear")
        self.display_clock()
        self.type_text("\033[36m" + "=" * 60)
        self.type_text("\033[32m               Welcome to Pressy OS Setup")
        self.type_text("\033[36m" + "=" * 60 + "\033[0m")

    def display_versions(self):
        """Show the available PressyOS versions."""
        self.display_clock()
        self.type_text("\n\033[36mAvailable PressyOS Versions:\033[0m")
        for version_id, version_name in self.collection.items():
            self.type_text(f"  \033[32m- {version_name} (ID: {version_id})\033[0m")
        self.type_text("\n\033[36mInstructions:\033[0m")
        self.type_text("\033[36mType the version ID to install (e.g., \033[32m1.0.0, Mini\033[36m).\033[0m")
        self.type_text("\033[36mThe system will guide you through the process.\033[0m")
        self.type_text("\033[36mPress Ctrl+C to stop the setup at any time.\033[0m\n")

    def simulate_installation(self, version_id):
        """Simulate installation with progress."""
        self.display_clock()
        self.type_text(f"\033[36mInstalling \033[32m{self.collection[version_id]}\033[36m...\033[0m")
        for i in range(3):
            self.display_clock()
            self.type_text("\033[36m[{}] {}\033[0m".format("=" * (i + 1), " " * (2 - i) + "Installing..."))
            time.sleep(1)
        self.display_clock()
        self.type_text("\033[36mInstallation Complete.\033[0m")
        time.sleep(1)

    def rainbow_effect(self):
        """Display a full-screen rainbow background effect."""
        rows, columns = os.popen("stty size", "r").read().split()
        full_screen = " " * int(columns) + "\n"
        for color in self.rainbow_colors:
            os.system("cls" if os.name == "nt" else "clear")
            for _ in range(int(rows)):
                print(f"{color}{full_screen}\033[0m", end="")
            time.sleep(0.3)
        os.system("cls" if os.name == "nt" else "clear")  # Reset to black background

    def fetch_and_execute(self, version_id):
        """Fetch and execute the OS script."""
        if version_id == "HTML":
            # Inform the user about the manual download for PressyOS Mini HTML edition
            self.type_text("\033[31m[Error]: This error only happens with the PressyOS Mini HTML edition.\033[0m")
            self.type_text("\033[31mPlease manually download the PressyOS Mini HTML script from the following URL:\033[0m")
            self.type_text(f"\033[35m{self.urls['HTML']}\033[0m")  # URL is purple
            self.type_text("\n\033[31mOnce downloaded, execute the script in Python.\033[0m")
            time.sleep(13.5)  # Increased time to 13.5 seconds for more reading time
            return

        if version_id == "Micro":
            # Execute embedded PressyOS Micro
            self.type_text("\033[36mLaunching \033[32mPressyOS Micro\033[36m...\033[0m")
            os_script = """
import os,time;d=os.getcwd();t=[]
while 1:
    c=input("> ").lower()
    if c=="help":print("help,date,todo,ls,cd,mkdir,rmdir,touch,cat,del,calc,exit")
    elif c=="date":print(time.ctime())
    elif c=="todo":
        while 1:
            a=input("Todo: ").lower()
            if a=="add":t.append(input("Add:"))
            elif a=="show":print(t)
            elif a=="rm":t.remove(input("Remove:"))
            elif a=="exit":break
            else:print("Invalid.")
    elif c=="ls":print("\\n".join(os.listdir()))
    elif c=="cd":os.chdir(input("Dir:"))
    elif c=="mkdir":os.makedirs(input("Dir:"),exist_ok=1)
    elif c=="rmdir":os.rmdir(input("Dir:"))
    elif c=="touch":open(input("File:"),'w').close()
    elif c=="cat":print(open(input("File:")).read())
    elif c=="del":os.remove(input("File:"))
    elif c=="calc":print(eval(input("Calc:")))
    elif c=="exit":break
    else:print("Unknown. Type help.")
"""
            exec_globals = {"__name__": "__main__"}
            exec(os_script, exec_globals)
            return

        if version_id == "Nano":
            # Execute embedded PressyOS Nano
            self.type_text("\033[36mLaunching \033[32mPressyOS Nano\033[36m...\033[0m")
            os_script = """
while True:
    c = input("> ").lower()
    if c == "help":
        print("Commands: help, date, exit")
    elif c == "date":
        import time
        print(time.ctime())
    elif c == "exit":
        break
    else:
        print("Unknown command. Type 'help'.")
"""
            exec_globals = {"__name__": "__main__"}
            exec(os_script, exec_globals)
            return

        # For other versions, fetch and execute as usual
        os_script_url = self.urls[version_id]
        response = requests.get(os_script_url)
        response.raise_for_status()
        os_script = response.text

        # Pre-launch rainbow effect
        self.rainbow_effect()

        # Execute the fetched script
        exec_globals = {"__name__": "__main__", "__file__": os_script_url}
        exec(os_script, exec_globals)

    def install_os(self, version_id):
        """Handle installation and execution of the selected OS."""
        if version_id not in self.collection:
            self.type_text("\033[31mInvalid version ID. Please enter a valid ID.\033[0m")
            return

        self.simulate_installation(version_id)
        self.fetch_and_execute(version_id)

    def run(self):
        """Run the setup application."""
        while True:
            try:
                self.display_header()
                self.display_versions()
                version_id = input("\033[36mEnter the version ID to install: \033[0m").strip()
                self.install_os(version_id)
                break  # Exit after successful execution
            except KeyboardInterrupt:
                self.type_text("\n\033[31mSetup interrupted. Exiting.\033[0m")
                break


# execution of evil people
if __name__ == "__main__":
    setup = PressyOSSetup() # hmm
    setup.run() # noooo do not run away baby
