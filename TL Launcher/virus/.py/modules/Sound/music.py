import os
import playsound
import time 

class Sound:
    def music():
        path = os.getcwd() + '/virus/.py/modules/Sound/music/rea.mp3'.replace('/', '\\')
        try:
            while True:
                playsound.playsound(path)
                time.sleep(0.6)
        except:
            pass
        
Sound.music()