from colorama import Fore

from audio.play import play_audio

print(Fore.GREEN+"starting audio test now")
play_audio("audio/audio_clips/audio_test/starting_audio_test.mp3")
play_audio("audio/audio_clips/audio_test/test.mp4")