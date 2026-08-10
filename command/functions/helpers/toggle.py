from colorama import Fore
from kasa import Discover, exceptions


async def toggle_plugs(name, ips, credential):
    for ip in ips:
        try:
            print(f"Connecting to {ip}...")
            dev = await Discover.discover_single(
                ip,
                username=credential["credentials"]["email"],
                password=credential["credentials"]["password"]
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
