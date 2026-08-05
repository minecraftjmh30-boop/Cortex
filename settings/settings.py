import json

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
        print("4) exit")

        choice = input("Enter your choice: ")
        match int(choice):
            case 1:
                edit_credentials()
            case 2:
                await discover()
            case 3:
                edit_lights()
            case 4:
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
    try:
        with open(path, "r") as f:
            json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        with open(path, "w") as f:
            if filename == "lights":
                json.dump({"lights": []}, f)
            elif filename == "credentials":
                json.dump({"credentials": {"email": "", "password": ""}}, f)
            else:
                json.dump({}, f)



def edit_lights():
    try_file("lights")
    lights_list = []

    while True:
        light_ip = input("Enter light ip (-1 to exit): ")
        if light_ip == "-1":
            break
        else:
            lights_list.append(light_ip)
    data = {"lights": lights_list}
    with open("settings/storage/lights.json", "w") as file:
        json.dump(data, file, indent=2)
    print(Fore.GREEN + "Lights updated successfully.")



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
    devices = await Discover.discover(on_discovered=print_dev_info, credentials=creds)
    return devices