import speech_recognition
import pyttsx3
import pygame
from command.keys.commands import commands

def start_cortex():
    print("Starting cortex...")
    cortex_listen()

def cortex_listen():
    recognizer = speech_recognition.Recognizer()  # voice recognizer
    print("Listening...")
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
                                command.execute()
                                found = True
                                break
                        if found:
                            break
                    if not found:
                        print("how can i help?")
                else:
                    print(f"Recognized: {text}")
        except speech_recognition.UnknownValueError:
            print("could not understand audio")
            continue

