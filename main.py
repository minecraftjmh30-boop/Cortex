import platform
current_os = platform.system()
if current_os == "Linux":
    #this suppresses ALSA lib errors
    import ctypes

    ERROR_HANDLER_FUNC = ctypes.CFUNCTYPE(None, ctypes.c_char_p, ctypes.c_int,
                                       ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p)

    def py_error_handler(filename, line, function, err, fmt):
        pass

    c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)

    try:
        asound = ctypes.cdll.LoadLibrary('libasound.so.2')
        asound.snd_lib_error_set_handler(c_error_handler)
    except OSError:
        pass

import asyncio


from colorama import Fore, init
from cortex import start_cortex
from settings.settings import menu
init(autoreset=True)




async def main():
    print(Fore.GREEN + """
    ,o888888o.        ,o888888o.     8 888888888o. 8888888 8888888888 8 8888888888   `8.`8888.      ,8' 
   8888     `88.   . 8888     `88.   8 8888    `88.      8 8888       8 8888          `8.`8888.    ,8'  
,8 8888       `8. ,8 8888       `8b  8 8888     `88      8 8888       8 8888           `8.`8888.  ,8'   
88 8888           88 8888        `8b 8 8888     ,88      8 8888       8 8888            `8.`8888.,8'    
88 8888           88 8888         88 8 8888.   ,88'      8 8888       8 888888888888     `8.`88888'     
88 8888           88 8888         88 8 888888888P'       8 8888       8 8888             .88.`8888.     
88 8888           88 8888        ,8P 8 8888`8b           8 8888       8 8888            .8'`8.`8888.    
`8 8888       .8' `8 8888       ,8P  8 8888 `8b.         8 8888       8 8888           .8'  `8.`8888.   
   8888     ,88'   ` 8888     ,88'   8 8888   `8b.       8 8888       8 8888          .8'    `8.`8888.  
    `8888888P'        `8888888P'     8 8888     `88.     8 8888       8 888888888888 .8'      `8.`8888. 
    """)
    while True:
        print("1) Start cortex")
        print("2) Config cortex")
        choice = input("enter:")
        try:
            choice_int = int(choice)
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number.")
            continue

        match choice_int:
            case 1:
                await start_cortex()
            case 2:
                await menu()
            case _:
                print("Wrong input")



if __name__ == "__main__":
    asyncio.run(main())

