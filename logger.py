#
# BY : KENMEIYOKI aka KILLIAN P.
# CREATION DATE : 2021-3-29 23:20 P.M UTC+1
# VERSION       : 0.0.1
# LICENSE       : MIT
# https://github.com/Kenmeiyoki/ken-logger

from colorama import Fore, Back, Style, init
init(autoreset=True)

def log(type, text):
    if ( type == 0 ):
        print(Fore.WHITE + "[" + Fore.BLACK + " ---- " + Fore.WHITE + "] " + Fore.BLACK + text)
    if ( type == 4 ):
        print(Fore.WHITE + "[" + Fore.RED + "FAILED" + Fore.WHITE + "] " + Fore.RED + text)
    if ( type == 2 ):
        print(Fore.WHITE + "[" + Fore.GREEN + "  OK  " + Fore.WHITE + "] " + Fore.GREEN + text)
    if ( type == 6 ):
        print(Fore.WHITE + "[" + Fore.YELLOW + " WARN " + Fore.WHITE + "] " + Fore.YELLOW + text)
    if ( type == 1 ):
        print(Fore.WHITE + "[" + Fore.BLUE + " ---- " + Fore.WHITE + "] " + Fore.BLUE + text)
    if ( type == 5 ):
        print(Fore.WHITE + "[" + Fore.MAGENTA + " TEMP " + Fore.WHITE + "] " + Fore.MAGENTA + text)
    if ( type == 9 ):
        print(Fore.WHITE + "[" + Fore.CYAN + " INFO " + Fore.WHITE + "] " + Fore.CYAN + text)
    if ( type == 7 ):
        print(Fore.WHITE + " ---- " + text)

log(2, "Module LOGGING Ready!")
