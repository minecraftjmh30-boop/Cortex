import os

from command.keys.load_custom_commands import load_custom_command_file


def c_c_menu():
    while True:
        print("===================")
        print("  Custom Commands")
        print("===================")
        print("1) Create New Command")
        print("2) Edit Command")
        print("3) Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
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
    import csv
    print("Creating A Custom Command")
    command_name = input("Enter command name: ")
    command_keys = []
    while True:
        command_key = input("Enter Key to activate command (-1 to exit): ")
        if command_key == "-1":
            break
        else:
            command_keys.append(command_key)

    # Save to CSV file
    csv_path = "settings/storage/custom_commands.csv"
    file_exists = os.path.isfile(csv_path)
    with open(csv_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Name', 'Keys', 'Function'])
        keys_str = ','.join(command_keys)
        writer.writerow([command_name, keys_str, 'Toggle'])
    print(f"Command '{command_name}' saved successfully.")



def edit_custom_command_menu():
    print("Choose Which Command to Edit")
    custom_commands = load_custom_command_file()
    for command in custom_commands:
        print(command)