import sys
import keyboard
from inputs import get_gamepad

from .keybinds import KEYBINDS
from networking.server_communicator import ServerCommunicator


def map_range(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = (value - leftMin) / leftSpan

    # Convert the 0-1 range into a value in the right range.
    return int(rightMin + (valueScaled * rightSpan))


class KeyboardHandler():
    def __init__(self, server_address, server_port):
        self.processor = InputProcessor(server_address, server_port)

    def start(self):
        keyboard.on_press(self._get_key_handler)

    def _get_key_handler(self, e):
        self.processor.process_keyboard_input(e.name)


class ControllerHandler():
    def __init__(self, server_address, server_port):
        self.stick = {'ABS_X': 0.0, 'ABS_Z': 0.0, 'ABS_RZ': 0.0}
        self.processor = InputProcessor(server_address, server_port)

    def start(self):
        while True:
            events = get_gamepad()
            for event in events:
                if event.code in self.stick:
                    self.stick[event.code] = event.state
                    self.processor.process_controller_input(
                        self.stick["ABS_X"], self.stick["ABS_Z"], self.stick["ABS_RZ"])


class InputProcessor:
    def __init__(self, server_address, server_port):
        self.server_communicator = ServerCommunicator(
            server_address, server_port)
        self.resolution = 255

    def process_keyboard_input(self, key):
        if key in KEYBINDS:
            if KEYBINDS[key] == 'quit':
                print("Telling the server to exit...")
                self.server_communicator.send_quit_command()
                return

            x, z = KEYBINDS[key]
            x *= self.resolution
            z *= self.resolution
            self.output_values(x, z)

    def process_controller_input(self, abs_x, abs_z, abs_rz):
        # Map the values to the correct range
        LSB = map_range(abs_x, -32767, 32767,
                        -self.resolution, self.resolution)
        LT = int(abs_z)
        RT = int(abs_rz)

        deadzone = 30
        if abs(LSB) < deadzone:
            LSB = 0

        self.output_values(RT - LT, -LSB)

    def output_values(self, x, z):
        print(f"\rProcessed | x: {x:>5} | z: {z:>5}", end="")

        # Send the data to the server
        self.server_communicator.send_data(x, z)
