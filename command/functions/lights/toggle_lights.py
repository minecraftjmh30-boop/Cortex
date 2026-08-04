import asyncio
from kasa import Discover

from audio.play import play_audio


async def toggle_lights():
    play_audio("test.mp4")
    print("Toggling lights")
