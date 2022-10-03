import time
import random
import math
import sys
from colorama import init, Fore, Back, Style

init()
FORE = [ Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE ]    # Sets the Foreground Colours
BACK = [ Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE ]    # Sets the Background Colours
BRIG = [ Style.DIM, Style.NORMAL, Style.BRIGHT ]                                                            # Sets the brightness styles

def print_s(str):                                                                                           # Defines a slow print
    for char in str:
            time.sleep(.03)
            sys.stdout.write(char)
            sys.stdout.flush()
    print()

def print_c(s, color=Fore.WHITE, brightness=Style.NORMAL, **kwargs):                                        # Defines a colour print
    print(f"{brightness}{color}{s}{Style.RESET_ALL}", **kwargs)

def print_s_c(str, color=Fore.WHITE, brightness=Style.NORMAL, **kwargs):                                    # Defines a slow colour print
    for char in str:
            time.sleep(.03)
            sys.stdout.write(f"{brightness}{color}{char}{Style.RESET_ALL}", **kwargs)
            sys.stdout.flush()
    print()




