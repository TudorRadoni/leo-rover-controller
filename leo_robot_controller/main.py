from input.input_handler import KeyboardHandler, ControllerHandler

if __name__ == "__main__":
    server_address = 'localhost'
    server_port = 12345

    keyboard_handler = KeyboardHandler(server_address, server_port)
    keyboard_handler.start()

    controller_handler = ControllerHandler(server_address, server_port)
    controller_handler.start()
