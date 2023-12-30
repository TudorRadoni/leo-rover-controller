# Movement controller for Leo Rover

A simple controller for Leo Rover that allows to control the rover's movement using:

- keyboard ⌨️
- gamepad 🎮 (currently supported: Xbox)

... in ROS Noetic (and tested in Gazebo, but should work on real robot too!).

## Features

- Control the rover's movement using **keyboard** ⌨️ or **gamepad** 🎮
- Mappable keys for keyboard (see [Mapping keys](#mapping-keys))
- Client (this app) sends commands to the server (Leo Rover) using sockets over TCP/IP
- Server (Leo Rover) receives commands and publishes them to ROS topics

## Mapping keys

The keys can be mapped in the `leo_robot_controller/input/keybinds.py` file. Here, you can find the default keybinds and customize them to your liking.

## Features to be implemented

- [ ] Add mappable gamepad controlls
- [ ] Add support for PS5 controller
- [ ] Add haptic feedback for gamepad

## URGENT TODO

TODO: Write the documentation!!!!!!!!!!
TODO: Hold controller value until next update
