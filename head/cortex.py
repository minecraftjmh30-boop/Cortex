import speech_recognition

from colorama import Fore


from head.ears import listen
from command.keys.commands import commands
from speech.speak import talk


async def start_cortex():
    print(Fore.GREEN + "Starting cortex...")
    await cortex()


async def cortex():
    recognizer = speech_recognition.Recognizer()
    print(Fore.GREEN + "Listening...")
    while True:
        text = await listen(recognizer)
        if text is None:
            continue
        if "cortex" in text:

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
        else:
            print(Fore.YELLOW + f"Recognized: {text}")
