import speech_recognition
import pyttsx3
import pygame
lights = False #program will eventually find if lights are on or off

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
                    if "lights" in text:

                        match lights:
                            case False:
                                print("Turning lights on now")
                                lights = True
                            case True:
                                print("Turning lights off now")
                                lights = False

                    else:
                        print("how can i help?")
                else:
                    print(f"Recognized: {text}")
        except speech_recognition.UnknownValueError:
            print("could not understand audio")
            continue

