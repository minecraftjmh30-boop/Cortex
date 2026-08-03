from command.Command import Command
from command.functions.lights.toggle_lights import toggle_lights
from command.functions.record_player.toggle_record_player import toggle_record_player

commands = ( Command("Toggle Lights",("lights", "toggle thy bulbs"), toggle_lights),
             Command("Toggle Record Player",("needle drop", "drop the needle"), toggle_record_player) )
