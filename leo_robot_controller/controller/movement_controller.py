import os
import keyboard
from .keybinds import KEYBINDS


class MovementController:
    def __init__(self):
        self.keybinds = KEYBINDS
        self.velocity = 1.0

    def start(self):
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
        for key, action in self.keybinds.items():
            keyboard.on_press_key(key, self._get_key_handler(key, action))

    def _get_key_handler(self, key, command):
        def handler(e):
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
            scaled_command = self._scale_command(command, self.velocity)
            formatted_command = "\n".join(f"{k}:  {self._format_dict(v)}" if k == 'linear' else f"{k}: {self._format_dict(v)}" for k, v in scaled_command.items())
            print(f'Command for key {key}:\n{formatted_command}', end='')
        return handler

    def _format_dict(self, d):
        return '{' + ', '.join(f"'{k}': {str(v):>4}" for k, v in d.items()) + '}'

    def _scale_command(self, command, scale):
        return {k: {kk: vv * scale for kk, vv in v.items()} for k, v in command.items()}
