import json
import os
import random

import sounddevice as sd
from colorama import Fore
from piper import PiperVoice


script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, "voice/en_GB-alan-medium.onnx")
voice = None
sample_rate = None
channels = 1


def _get_voice():
    global voice, sample_rate
    if voice is None:
        try:
            voice = PiperVoice.load(model_path)
            sample_rate = voice.config.sample_rate
        except Exception as e:
            print(f"Failed to load voice model: {e}")
            raise
    return voice


def talk(text):
    if text == "basic_dialog":
        text = basic_dialog()
    print(Fore.GREEN+text)
    v = _get_voice()
    with sd.RawOutputStream(samplerate=v.config.sample_rate, channels=channels, dtype='int16') as stream:

        for chunk in v.synthesize(text):

            stream.write(chunk.audio_int16_bytes)



def basic_dialog():
    dialog_path = os.path.join(script_dir, "dialog/basic.json")
    with open(dialog_path) as file:
        data = json.load(file)
    lines = data.get("actions", ["ok"])
    random_line = random.randint(0, len(lines) - 1)
    dialog = lines[random_line]
    return dialog