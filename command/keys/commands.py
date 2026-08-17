from audio.play import play_audio
from command.Command import Command
from command.functions.actions.toggle import toggle
from command.functions.greetings.introduction import introduction
from command.functions.test.audio_test import start_audio_test

commands = [
             Command("Audio Test", ("test audio", "audio test"), start_audio_test),
             Command("Introduction",("introduce yourself","who are you"), introduction),
             ]

