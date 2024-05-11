import ctypes
import time
import keyboard
from colorama import init
from termcolor import colored
import datetime
from datetime import datetime
import os

init()
loops = 0
scriptversion = ('v1.1.7')

SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
def splash():
    print(colored(f'   _______________       ____  _   ____    _____   ________', 'red'))
    print(colored(f'  / ____/_  __/   |     / __ \/ | / / /   /  _/ | / / ____/', 'red'))
    print(colored(f' / / __  / / / /| |    / / / /  |/ / /    / //  |/ / __/   ', 'red'))
    print(colored(f'/ /_/ / / / / ___ |   / /_/ / /|  / /____/ // /|  / /___   ', 'red'))
    print(colored(f'\____/_/_/ /_/ _|_|___\____/_/ |_/_____/___/_/_|_/_____/   ', 'red'))
    print(colored(f'   /   |  / | / /_  __/  _/    /   |  / ____/ //_/         ', 'red'))
    print(colored(f'  / /| | /  |/ / / /  / /_____/ /| | / /_  / , <           ', 'red'))
    print(colored(f' / ___ |/ /|  / / / _/ /_____/ ___ |/ __/ / /| |           ', 'red'))
    print(colored(f'/_/  |_/_/ |_/ /_/ /___/    /_/  |_/_/   /_/ |_|           ', 'red'))
    print(colored(f' {scriptversion}                          Made by iceyyylol', 'red'))
    print(colored(f'                                                           ', 'red'))
splash()

print(colored(f'[!] Script will be active in 5s', 'yellow'))
print(colored(f'                                          ', 'yellow'))

time.sleep(5)
print(colored(f'[!] Script Active', 'red'))
print(colored(f'                                          ', 'yellow'))

while keyboard.is_pressed('q') == False:
    PressKey(0x11)
    time.sleep(0.43932)
    ReleaseKey(0x11)
    loops =+ 1
    now = datetime.now()
    timenow = now.strftime('%H:%M:%S')
    os.system('cls')
    splash()
    print(colored(f'[{timenow}] Looped | Loop: {loops}', 'green'))
    time.sleep(300)