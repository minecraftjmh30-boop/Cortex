import platform

from settings.linux_fix import linux_fix

current_os = platform.system()
if current_os == "Linux":
    linux_fix()

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

