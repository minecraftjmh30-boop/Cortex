import json

from kasa import Discover, exceptions

from audio.play import audio
from command.functions.helpers.toggle import toggle_plugs
from speech.speak import talk


async def toggle_record_player():
    talk("basic_dialog")

    try:
        with open("settings/storage/credentials.json") as cred_file:
            credentials = json.load(cred_file)
        with open("settings/storage/record_player.json") as record_player_file:
            data = json.load(record_player_file)
            # Access the list of IPs using the key
            record_player_ips = data.get("record_player", [])

            if isinstance(record_player_ips, str):  # Handle the case where it's a single string
                record_player_ips = [record_player_ips]

    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading configuration: {e}")
        return

    await toggle_plugs("Record Player", record_player_ips, credentials)