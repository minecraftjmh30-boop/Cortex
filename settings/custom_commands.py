from command.keys.load_custom_commands import load_custom_command_file


def c_c_menu():
    while True:
        print("===================")
        print("  Custom Commands")
        print("===================")
        print("1) Create New Command")
        print("2) Edit Command")
        print("3) Exit")
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                create_custom_command()
            case 2:
                edit_custom_command_menu()
            case 3:
                return
            case _:
                print("Invalid Command")




def create_custom_command():
    print("Creating A Custom Command")
    command_name = input()
    command_keys = []
    while True:
        command_key = input("Enter Key to activate command(-1 to exit): ")
        if command_key == -1:
            break
        else:
            command_keys.append(command_key)



def edit_custom_command_menu():
    print("Choose Which Command to Edit")
    custom_commands = load_custom_command_file()
    for command in custom_commands:
        print(command)