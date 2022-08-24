from selectd.selection import Selection
from pynput.keyboard import Key, Listener, KeyCode

combo = [Key.ctrl, KeyCode.from_char('$')]

class Combo():
    def __init__(self):
        self.pressed = []
        self.in_combo = False
        self.selection = Selection()
        self.listener = Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()

    def on_press(self,key):
        self.pressed.append(key)

    def on_release(self, key):
        self.pressed = list(filter(lambda x: x != key, self.pressed))

    def on_combo(self, callback):
        selected = self.selection.get_selected_text().decode('utf-8')
        callback(selected)


    def keys_in_pressed(self, keys):
        for key in keys:
            if key not in self.pressed:
                return False
        return True

    def listen(self, callback):
        while True:
            if self.in_combo:
                if not self.keys_in_pressed(combo):
                    self.pressed = []
                    self.in_combo = False
                    break
            else:
                if self.keys_in_pressed(combo):
                    self.in_combo = True
        self.on_combo(callback)
