import asyncio
import json
import os
from kasa import Discover, exceptions  # Added exceptions

from audio.play import audio


async def toggle_lights():
    print("toggling lights")
    audio("basic")
    try:
        with open("settings/storage/credentials.json") as cred_file:
            credentials = json.load(cred_file)
        with open("settings/storage/lights.json") as lights_file:
            data = json.load(lights_file)
            # Access the list of IPs using the "lights" key
            light_ips = data.get("lights", [])

            if isinstance(light_ips, str):  # Handle the case where it's a single string
                light_ips = [light_ips]

    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading configuration: {e}")
        return

    # Ensure TZ is set for Linux environments where timezone detection might fail
    if os.name != 'nt' and 'TZ' not in os.environ:
        os.environ['TZ'] = 'UTC'

    for ip in light_ips:
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
            print(f"Could not connect to light at {ip}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred for {ip}: {e}")