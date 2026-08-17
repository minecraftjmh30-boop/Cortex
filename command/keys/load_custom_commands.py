#get custom_commands.json if available
#add all custom commands to command class

def load_commands():
    try:
        with open("settings/storage/custom_commands.json") as file:
            file

    except(FileNotFoundError):
        print("no commands")