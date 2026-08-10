import asyncio
import json
import os
from kasa import Discover, exceptions  # Added exceptions

from audio.play import audio
from command.functions.helpers.toggle import toggle_plugs
from speech.speak import talk


async def toggle_lights():
    talk("basic_dialog")

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

    await toggle_plugs("Lights", light_ips, credentials)
