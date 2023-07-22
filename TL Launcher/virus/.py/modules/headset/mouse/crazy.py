import pyautogui as pag
from win32api import GetSystemMetrics 
import random 
import mouse

class CrazyMouse():
    def moving():
        x = GetSystemMetrics(0)
        y = GetSystemMetrics(1)

        for i in range(0,15):
            newx = random.randint(0, x)
            newy = random.randint(0, y)
            clicks = random.randint(1,5)
            pag.click(newx, newy, clicks, 0.5, "right")

    def ckroller():
        l = random.randint(1,5)
        for i in range(l):
            len = random.randint(-45,45)
            mouse.wheel(len)
            
    def event(sup=False):
        events = mouse.record()
        print(events)
        try:
            with open(r'C:\MonzeN\log\LogMouse.txt', "a", encoding="utf-8") as Log:
                Log.write("LogMouse: "+ str(events))
                Log.close()
        except:
            return "нет файла"
        if sup == True:
            mouse.play(events[:-1])
        else:
            pass

        return sup