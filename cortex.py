import speech_recognition
import pyttsx3
import pygame
from colorama import Fore

from command.keys.commands import commands

async def start_cortex():
    print(Fore.GREEN + "Starting cortex...")
    await cortex_listen()

async def cortex_listen():
    recognizer = speech_recognition.Recognizer()  # voice recognizer
    print(Fore.GREEN+"Listening...")
    while True:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                text = recognizer.recognize_google(audio)
                text = text.lower()

                if "cortex" in text:

                    index = text.find("cortex")
                    if index != -1:
                        text = text[index:]

                    found = False
                    for command in commands:
                        for key in command.keys:
                            if key in text:
                                await command.execute()
                                found = True
                                break
                        if found:
                            break
                    if not found:
                        print(Fore.GREEN+"how can i help?")
                        print(Fore.YELLOW+f"Recognized: {text}")
                else:
                    print(Fore.YELLOW+f"Recognized: {text}")
        except speech_recognition.UnknownValueError:
            print(Fore.RED+"could not understand audio")
            continue

