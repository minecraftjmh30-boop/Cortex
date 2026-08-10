from colorama import Fore

from audio.play import play_audio
from speech.speak import talk


def start_audio_test():
    talk("starting audio test now")
    play_audio("audio/audio_clips/audio_test/test.mp4")