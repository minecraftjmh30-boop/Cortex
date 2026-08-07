import json
import os

from colorama import Fore
from kasa import Credentials, Discover, exceptions

from command.functions.lights.toggle_lights import toggle_lights


async def menu():
    while True:
        print("============")
        print("  settings")
        print("============")
        print("1) Edit credentials")
        print("2) discover ips for kasa")
        print("3) edit lights")
        print("4) edit record player")
        print("5) exit")

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



def try_file(filename):
    path = f"settings/storage/{filename}.json"
    needs_reset = False
    try:
        with open(path, "r") as f:
            data = json.load(f)
            if filename == "lights" and "lights" not in data:
                needs_reset = True
            elif filename == "credentials" and "credentials" not in data:
                needs_reset = True
            elif filename == "record_player" and "record_player" not in data:
                needs_reset = True
    except (FileNotFoundError, json.JSONDecodeError):
        needs_reset = True

    if needs_reset:
        with open(path, "w") as f:
            if filename == "lights":
                json.dump({"lights": []}, f)
            elif filename == "credentials":
                json.dump({"credentials": {"email": "", "password": ""}}, f)
            elif filename == "record_player":
                json.dump({"record_player": []}, f)
            else:
                json.dump({}, f)



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
    # Ensure TZ is set for Linux environments where timezone detection might fail
    if os.name != 'nt' and 'TZ' not in os.environ:
        os.environ['TZ'] = 'UTC'

    devices = await Discover.discover(on_discovered=print_dev_info, credentials=creds)
    return devices