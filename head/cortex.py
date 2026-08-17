import speech_recognition

from colorama import Fore


from head.ears import listen
from command.keys.commands import commands
from command.keys.load_custom_commands import load_commands
from speech.speak import talk


async def start_cortex():
    load_commands()
    print(Fore.GREEN + "Starting cortex...")
    recognizer = speech_recognition.Recognizer()

    while True:
        heard = await cortex_listen(recognizer)
        if heard is None:
            continue
        else:
            await process_command(heard)



async def cortex_listen(recognizer):
    print(Fore.GREEN + "Listening...")
    text = await listen(recognizer)
    if text is None:
        return None
    if "cortex" in text:
        return text
    else:
        print(Fore.YELLOW + f"Recognized: {text}")
        return None


async def process_command(text):
    index = text.find("cortex")
    if index != -1:
        text = text[index:]

    found = False
    for command in commands:
        for key in command.keys:
            if key in text:
                await command.execute()
                found = True
                break
        if found:
            break
    if not found:
        talk("how can i help")
        print(Fore.YELLOW + f"Recognized: {text}")