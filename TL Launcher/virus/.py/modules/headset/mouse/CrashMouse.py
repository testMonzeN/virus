import pyautogui as pag

class CrashMouse():
    def mouse():
        while True:
            x, y = pag.position()
            if x != 0 and y != 0:
                pag.moveTo(0,0)
                pag.PAUSE = 0.1
    
