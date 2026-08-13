#move cortexs hearing to here

import speech_recognition
from colorama import Fore





async def listen(recognizer):
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio_heard = recognizer.listen(mic)

            text = recognizer.recognize_google(audio_heard)
            text = text.lower()
        return text

    except speech_recognition.UnknownValueError:
        print(Fore.RED + "could not understand audio")
        return None