from colorama import Fore

from audio.play import audio


def introduction():
    print(Fore.GREEN+"My name is Cortex, the virtual assistant created by Jack Hackett and Lincoln Stuller. "
                     "I can operate lights, appliances, and other such electronical devices like Mr Stullers record player."
                     "If there is anything I can help you with, just say cortex.")
    audio("intro")