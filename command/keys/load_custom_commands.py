#get custom_commands.csv if available
#add all custom commands to command class
import csv
import functools

from colorama import Fore

from command.Command import Command
from command.keys import commands as cmd_module
from command.functions.actions.toggle import toggle

def load_commands():
    try:
        with open("settings/storage/custom_commands.csv", mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['Name']
                keys = tuple(k.strip() for k in row['Keys'].split(','))
                func_name = row['Function']
                
                if func_name == "Toggle":
                    # We need to extract the target name from the Command name or similar.
                    # Based on CSV: Toggle_Lights -> target is "lights"
                    target = name.lower().replace("toggle_", "")
                    func = functools.partial(toggle, target)
                else:
                    print(Fore.YELLOW + f"Unknown function: {func_name} for command {name}")
                    continue
                
                cmd_module.commands.append(Command(name, keys, func))

    except FileNotFoundError:
        print(Fore.RED + "no commands found")
    except Exception as e:
        print(Fore.RED + f"Error loading custom commands: {e}")

def load_custom_command_file():
    try:
        custom_commands = ()
        with open("settings/storage/custom_commands.csv", mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                command = ()
                name = row['Name']
                keys = tuple(k.strip() for k in row['Keys'].split(','))
                func_name = row['Function']

                command.append(name, keys, func_name)
                custom_commands.append(command)
        return custom_commands

    except FileNotFoundError:
        print(Fore.RED + "no commands found")
    except Exception as e:
        print(Fore.RED + f"Error loading custom commands: {e}")