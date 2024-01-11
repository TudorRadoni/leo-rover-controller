# Movement controller for Leo Rover

A simple controller for Leo Rover that allows to control the rover's movement using:

- keyboard ⌨️
- gamepad 🎮 (tested: Xbox One, but should work with any controller)

... in ROS Noetic (and tested in Gazebo, but should work on real robot too!).

> **Note:** *A more detailed documentation can be found in the `docs/` directory. There is a more detailed description and more technical details, as well as a walkthrough of setting up the robot and running the controller.*

## Features

- Control the rover's movement using **keyboard** ⌨️ or **gamepad** 🎮
- Velocity sensitive movement (on gamepads)
- Mappable keys for keyboard (see [Mapping keys](#mapping-keys))
- Client (this app) sends commands to the server (Leo Rover) using sockets over TCP/IP
- Server (Leo Rover) receives commands and publishes them to ROS topics

## Mapping keys

The keys can be mapped in the `leo_robot_controller/input/keybinds.py` file. Here, you can find the default keybinds and customize them to your liking.

## Features to be implemented

- [ ] Add mappable gamepad controlls
- [ ] Add haptic feedback for gamepad
