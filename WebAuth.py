from bs4 import BeautifulSoup
import time
import pandas as pd
import requests
from requests import RequestException
import os
import sys
import colorama
import pyfiglet
import random
from colorama import Fore
import subprocess
from urllib.parse import urlparse



# Timers


def two_secs():
    time.sleep(2)


def four_secs():
    time.sleep(4)


def eight_secs():
    time.sleep(8)


# Tricks
def Quit():
    sys.exit(1)


def Restart_The_Tool():
    os.system("python WebAuth.py")

# A Set Of Options


def options():
    opts = {1: 'Rerun The Tool',
            2: 'Quit',
            }
    for keys in opts.keys():
        print(keys, opts[keys])
    choice = (int(input("\n\nKINDLY SELECT AN OPTION!\n  ====>>:   ")))

    # A Little Magic
    if choice == 1:
        two_secs()
        print("Hold ON PLEASE!...")
        Restart_The_Tool()

    elif choice == 2:
        four_secs()
        print(" PLEASE WAIT ...")
        Quit()

    else:
        print("Keyboard EError!")
        quit()


# COLORS
B = Fore.BLUE
R = Fore.RED
G = Fore.GREEN
Y = Fore.YELLOW
CY = Fore.CYAN
RS = Fore.RESET
MG = Fore.MAGENTA


RAINBOW = (B, R, G, Y, CY, MG, )

# Banner


def BANNER():
    f = pyfiglet.figlet_format("W-Auth", font="banner3-D")
    print(random.choice(RAINBOW)+f)
    print(MG+"Author: Orlando The Maker \n"
             "Name: Jeremiah Abdulsalam\n"
             "Country: Nigeria\n"
             "Phone: +2349016293765"+RS)
    print(random.choice(RAINBOW)+"Github: https://github.com/OrlandoTheMaker\n"
                                 "LinkedIn: https://www.linkedin.com/in/orlando-the-maker-50b21a277/\n"
                                 "Twitter: https://twitter.com/Orlando13140")


# Clear Screen
def cls():
    subprocess.call('cls', shell=True)


# The Engine
def WebAuth():
    The_Link = input('Enter The Link Here: ')
    Parsed_Link = "https://"+The_Link

    try:
        res = requests.get(Parsed_Link)
        soup = BeautifulSoup(res.text, 'html.parser')
        STATUS = res.status_code

        for i in soup.findAll('a'):
            links = i.get('href')
            DATA = {
                "STATUS": [STATUS],
                "LINK": [links],
            }
            results = pd.DataFrame(DATA)
            two_secs()
            print(results)

    except requests.exceptions.ConnectionError:
        print("Error In Connecting To Site!")


BANNER()
four_secs()
cls()
print('\n')
WebAuth()
print('\n\n All Done BOSS!!\n\n')
options()
