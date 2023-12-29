import keyboard
from .keybinds import KEYBINDS

class MovementController:
    def __init__(self):
        self.keybinds = KEYBINDS

    def start(self):
        for key, action in self.keybinds.items():
            keyboard.on_press_key(key, self._get_key_handler(key, action))

    def _get_key_handler(self, key, action):
        def handler(e):
            print(f'\r\033[KAction: {action} ({key})', end='')
        return handler
