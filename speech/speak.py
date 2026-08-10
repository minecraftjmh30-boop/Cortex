import json
import os
import random

import sounddevice as sd
from colorama import Fore
from piper import PiperVoice


script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, "voice/en_GB-alan-medium.onnx")
voice = PiperVoice.load(model_path)
sample_rate = voice.config.sample_rate
channels = 1


def talk(text):
    if text == "basic_dialog":
        text = basic_dialog()
    print(Fore.GREEN+text)
    with sd.RawOutputStream(samplerate=sample_rate, channels=channels, dtype='int16') as stream:

        for chunk in voice.synthesize(text):

            stream.write(chunk.audio_int16_bytes)



def basic_dialog():
    with open("speech/dialog/basic.json") as file:
        data = json.load(file)
    lines = data.get("actions", "ok")
    random_line = random.randint(0,len(lines) - 1)
    dialog = lines[random_line]
    return dialog