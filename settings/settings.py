import json

from colorama import Fore
from kasa import Credentials, Discover, exceptions

from settings.helper import try_file


async def menu():
    while True:
        print("============")
        print("  settings")
        print("============")
        print("1) Edit Credentials")
        print("2) Discover IPs for kasa")
        print("3) Edit Lights")
        print("4) Edit Record Player")
        print("5) Exit")

        choice = input("Enter your choice: ")
        try:
            choice_int = int(choice)
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number.")
            continue

        match choice_int:
            case 1:
                edit_credentials()
            case 2:
                await discover()
            case 3:
                edit_types("lights")
            case 4:
                edit_types("record_player")
            case 5:
                return
            case _:
                print(Fore.RED + "Wrong input")



def edit_credentials():
   try_file("credentials")
   email = input("Enter your email: ")
   password = input("Enter your password: ")
   with open("settings/storage/credentials.json") as r_file:
       cred = json.load(r_file)
       cred["credentials"]["email"] = email
       cred["credentials"]["password"] = password
       with open("settings/storage/credentials.json", "w") as w_file:
           json.dump(cred, w_file)
       return None




#Delete
def edit_types(command_type):
    try_file(command_type)
    type_list = []

    while True:
        command_ip = input(f"Enter {command_type} ip (-1 to exit): ")
        if command_ip == "-1":
            break
        else:
            type_list.append(command_ip)
    data = {f"{command_type}": type_list}
    with open(f"settings/storage/{command_type}.json", "w") as file:
        json.dump(data, file, indent=2)
    print(Fore.GREEN + f"{command_type} updated successfully.")



async def discover():
    print(Fore.GREEN + "discovering ips for kasa...")
    print("REMEMBER IPS FOR KASA")

#AI-Generated except executions
    async def print_dev_info(dev):
        try:
            await dev.update()
            print(f"Discovered {dev.alias} (ip: {dev.host}) (model: {dev.model})")
        except exceptions.AuthenticationError:
            print(Fore.RED + f"Authentication failed for {dev.host}. Check your credentials.")
        except exceptions.KasaException as e:
            print(Fore.RED + f"Error connecting to {dev.host}: {e}")
    try:
        with open("settings/storage/credentials.json") as file:
            cred = json.load(file)
            creds = Credentials(cred["credentials"]["email"], cred["credentials"]["password"])
    except (FileNotFoundError, KeyError) as e:
        print(Fore.RED + f"Error loading credentials: {e}")
        return None
    devices = await Discover.discover(on_discovered=print_dev_info, credentials=creds)
    return devices