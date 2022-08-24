import json
import time
import webview
import os
import pyclip
from selectd.combo import Combo
from selectd.process import focus_process, get_active_window
from pynput.keyboard import Controller, Key

def escape_quotes(string):
    return string.replace("\\", "\\\\").replace('"', '\\"').replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def load_html(window, selection):
    path = os.path.dirname(os.path.realpath(__file__))
    with open('%s/html/test.html' % path, 'r') as f:
        html = f.read().replace("{SELECTION}", escape_quotes(selection))
        window.load_html(html)

combo = Combo()
def hide_window(obj, action = None):
    obj.window.hide()
    if (action != None):
        time.sleep(0.1)
        if action["action"] == "copy":
            pyclip.copy(action["text"])
        elif action["action"] == "insert":
            keyboard = Controller()
            keyboard.tap(Key.backspace)
            keyboard.type(action["text"])
    combo.listen(obj.open_at_cursor)

class Window():
    def __init__(self):
        self.window = None
    def check_communication(self):
        communication = self.window.get_elements("#communicate_action")[0]
        if (len(communication["childNodes"]) == 0):
            return None
        return json.loads(communication["childNodes"][0]["data"])

    def check_focus(self):
        time.sleep(1)
        action = None
        while True:
            time.sleep(0.3)
            action = self.check_communication()
            if action != None:
                break
            if get_active_window() != "python3":
                break
        hide_window(self, action)

    def create_window(self):
        if self.window is None:
            self.window = webview.create_window('selectdpanel', width=300, height=400, frameless=True, easy_drag=False, on_top=True)
            webview.start(hide_window, self)


    def open_at_cursor(self, selection):
        load_html(self.window, selection)
        self.window.show()
        time.sleep(0.3)
        focus_process("selectdpanel")
        self.check_focus()
