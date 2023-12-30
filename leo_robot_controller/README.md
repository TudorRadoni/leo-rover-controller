# How to use the robot controller

## Starting the controller

Assuming you have the Leo Rover ROS packages installed, you can run the controller on the robot or on WSL.

Steps for running **server** on `WSL2`, inside `Ubuntu 20.04` and **client** in `Windows 11` (tested, works):

Linux:

1. Get Leo up and running (the scripts in `../scripts/` should help you with that)
2. `cd` into `server/` and run `python3 move.py`

Windows:

1. `python main.py`

## Using the controller

Use `WASD` or the arrow keys to move the robot around (or your custom keybinds). Press `esc` to exit.

If you have a controller, use left stick to move left/right, left trigger to move backwards and right trigger to move forwards.
