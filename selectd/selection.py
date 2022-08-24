import pyclip
from pynput.keyboard import Key, Controller
from selectd.process import get_active_window

copy_commands = {
    "gnome-terminal-": [Key.ctrl, Key.shift, 'c'],
    "default": [Key.ctrl, 'c'],
}


class Selection:
    def __init__(self):
        self.clipboard = None
        self.keyboard = Controller()

    def save_clipboard(self):
        self.clipboard = pyclip.paste()

    def restore_clipboard(self):
        pyclip.copy(self.clipboard)
        self.clipboard = None

    def get_selected_text(self):
        self.save_clipboard()
        command = copy_commands.get(get_active_window(), copy_commands["default"])
        for key in command:
            self.keyboard.press(key)
        for key in command:
            self.keyboard.release(key)
        selected = pyclip.paste()
        self.restore_clipboard()
        return selected