from audio.play import play_audio
from command.Command import Command
from command.functions.intro.introduction import introduction
from command.functions.lights.toggle_lights import toggle_lights
from command.functions.record_player.toggle_record_player import toggle_record_player
from command.functions.test import audio_test

commands = ( Command("Toggle Lights",("lights", "toggle thy bulbs"), toggle_lights),
             Command("Toggle Record Player",("needle drop", "drop the needle"), toggle_record_player),
             Command("Audio Test", ("test audio", "audio test"), audio_test),
             Command("Introduction",("introduce yourself","who are you"), introduction),
             )

