from audio.play import play_audio
from command.Command import Command
from command.functions.helpers.toggle import toggle
from command.functions.intro.introduction import introduction
from command.functions.test.audio_test import start_audio_test

commands = ( Command("Toggle Lights",("lights", "toggle thy bulbs"), toggle("lights")),
             Command("Toggle Record Player",("needle drop", "drop the needle"), toggle("record_player")),
             Command("Audio Test", ("test audio", "audio test"), start_audio_test),
             Command("Introduction",("introduce yourself","who are you"), introduction),
             )

