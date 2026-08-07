import json

from kasa import Discover, exceptions

from audio.play import audio


async def toggle_record_player():
    print("Record Player has not been configured at this time")
    audio("basic")
    try:
        with open("settings/storage/credentials.json") as cred_file:
            credentials = json.load(cred_file)
        with open("settings/storage/record_player.json") as lights_file:
            data = json.load(lights_file)
            # Access the list of IPs using the "lights" key
            record_player_ips = data.get("lights", [])

            if isinstance(record_player_ips, str):  # Handle the case where it's a single string
                record_player_ips = [record_player_ips]

    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading configuration: {e}")
        return

    for ip in record_player_ips:
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
            print(f"Could not connect to record player at {ip}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred for {ip}: {e}")