import socket
import struct


class ServerCommunicator:
    def __init__(self, server_address, server_port):
        self.server_address = server_address
        self.server_port = server_port

    def send_data(self, x, z):
        s = socket.socket()  # Create a client socket        
        s.connect((self.server_address, self.server_port)) # Connect to the server

        data = struct.pack('ff', x, z)  # Pack the data into a binary format

        s.send(data)  # Send the data to the server
        s.close()  # Close the socket

    def send_quit_command(self):
        # Pack a special quit command
        # Use a special value to indicate quit
        # 40000 is outside the range of the joystick
        self.send_data(-40000.0, -40000.0)
