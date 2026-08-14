import json

from colorama import Fore
from kasa import Discover, exceptions

from head.speech.speak import talk


async def toggle(name):
    talk("basic_dialog")

    try:
        with open("settings/storage/credentials.json") as cred_file:
            credentials = json.load(cred_file)
        with open(f"settings/storage/{name}.json") as ip_file:
            data = json.load(ip_file)
            # Access the list of IPs
            toggle_ips = data.get(f"{name}", [])

            if isinstance(toggle_ips, str):  # Handle the case where it's a single string
                toggle_ips = [toggle_ips]

    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading configuration: {e}")
        return

    for ip in toggle_ips:
        try:
            print(f"Connecting to {ip}...")
            dev = await Discover.discover_single(
                ip,
                username=credentials["credentials"]["email"],
                password=credentials["credentials"]["password"]
            )
            await dev.update()

            if dev.is_on:
                await dev.turn_off()
                print(f"Turned off {dev.alias}")
            else:
                await dev.turn_on()
                print(f"Turned on {dev.alias}")

        except exceptions.KasaException as e:
            print(Fore.RED+f"Could not connect to {name} at {ip}: {e}")
        except Exception as e:
            print(Fore.RED+f"An unexpected error occurred for {ip}: {e}")






