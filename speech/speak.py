import os
import sounddevice as sd
from piper import PiperVoice


script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, "en_GB-alan-medium.onnx")
voice = PiperVoice.load(model_path)
sample_rate = voice.config.sample_rate
channels = 1

text = "Streaming audio directly to your speakers with sounddevice is incredibly fast."

with sd.RawOutputStream(samplerate=sample_rate, channels=channels, dtype='int16') as stream:

    for chunk in voice.synthesize(text):

        stream.write(chunk.audio_int16_bytes)
