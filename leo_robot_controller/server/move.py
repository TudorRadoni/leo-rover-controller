import os
import sys

import socket
import struct

import rospy
from geometry_msgs.msg import Twist

class NetworkListener:
    def __init__(self, port):
        self.s = socket.socket()
        self.port = port
        self.s.bind(('', self.port))
        self.s.listen(5)

    def receive_data(self):
        c, addr = self.s.accept()
        data = c.recv(1024)
        x, z = struct.unpack('ii', data)

        if x == -40000 and z == -40000:
            raise SystemExit("Quit signal received")

        term_width = os.get_terminal_size().columns # get the width of the terminal
        print(f'\rReceived | x:{x:>5} | y:{z:>5} |', end='')
        
        return x, z


class RosPublisher:
    def __init__(self, topic):
        rospy.init_node('movement_publisher')
        self.pub = rospy.Publisher(topic, Twist, queue_size=10)

    def send_data(self, x, z):
        msg = Twist()
        msg.linear.x = x
        msg.angular.z = z
        self.pub.publish(msg)


if __name__ == '__main__':
    network_listener = NetworkListener(port=12345)
    ros_publisher = RosPublisher('/controllers/diff_drive/cmd_vel')
    
    try:
        while True:
            x, z = network_listener.receive_data()
            ros_publisher.send_data(x, z)
    
    except KeyboardInterrupt:
        print("\nYou pressed Ctrl+C! Stopping the server.")
        sys.exit(0)
        