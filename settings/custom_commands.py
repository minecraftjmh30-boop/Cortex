

def custom_command_menu():
    print("1) Create New Command")
    print("2) Edit Command")
    print("3) Exit")




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



def edit_custom_command(command):
    print("")