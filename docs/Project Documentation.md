# RCS Project - Documentation

## ROS Installation

I used Ubuntu 20.04 LTS for this project. I followed the instructions on the ![ROS website](http://wiki.ros.org/noetic/Installation/Ubuntu) to install ROS Noetic. I used the "Desktop-Full Install" option.

## Choosing a robot

To choose a robot, I looked at the ![ROS Robots list with tag #noetic](https://robots.ros.org/tags/#noetic).

I eventually chose the ![Leo Rover](https://robots.ros.org/leo-rover/).

## Installing the robot

```bash
mkdir -p ~/<robot_name>_ws/src
cd ~/<robot_name>_ws/src
git clone <robot_git_repo>
rosdep install -r -y --from-paths . --ignore-src
cd ..
catkin_make
```

## Running the robot

You can use two ways here:

### Manual way

```bash
source ~/leo_ws/devel/setup.bash
export LEO_GAZEBO_DESCRIPTION=$(rospack find leo_gazebo)/urdf/description.gazebo.xacro
cd ~/leo_ws/src/leo/leo_gazebo/launch/
roslaunch leo_gazebo empty_world.launch # open Gazebo with Leo in an empty world
```

### Using the scripts I made

> **Note:** *You must have leo_ws in your home directory for this method to work!*

```bash
chmod u+x ./init_ros_and_leo
chmod u+x ./launch_leo

./init_ros_and_leo
./launch_leo
```

## The idea for the controller

I thought that it would be cool to have a controller that could control the robot using a gamepad. Later, I wanted to also add keyboard support (should probably do this before the gamepad, since it's easier) and mappable controls . Since I was running the robot in WSL, I figured it wouldn't be so cool to make usb and drivers work. Therefore, I came up with this:

- The robot will run a server that will listen for commands on a socket
- The client will send commands to the server running on the robot via that socket

This way, the client can run on any OS and be a black box for the robot. Furthermore, this will work for the real robot too, since it does the same thing as in simulation and doesn't require any additional drivers.

## Useful links (that I used to make this)

### ROS

- [ROS Noetic Installation - Ubuntu](http://wiki.ros.org/noetic/Installation/Ubuntu)
- [ROS Noetic Tutorials](http://wiki.ros.org/ROS/Tutorials)
- [Create Catkin Workspace](http://wiki.ros.org/catkin/Tutorials/create_a_workspace)
- [Create Catkin Package](http://wiki.ros.org/catkin/Tutorials/CreatingPackage)
- [ROS Python Publisher/Subscriber Tutorial](http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29)
- [Odometry Message](http://docs.ros.org/en/api/nav_msgs/html/msg/Odometry.html)

### Leo Rover

- [Leo Rover ROS Wiki](http://wiki.ros.org/Robots/Leo%20Rover)
- [Leo Rover Simulator GitHub Repository](https://github.com/LeoRover/leo_simulator)

### Testing more robots (just for fun)

#### TIAGo

- [TIAGo Robot Simulation Files](http://wiki.ros.org/Robots/TIAGo#Simulation_files)

#### Copernicus

- [Copernicus Robot Information](http://wiki.ros.org/Robots/Copernicus)
- [Launching a Gazebo Simulation Environment Tutorial](http://wiki.ros.org/Robots/Copernicus/Tutorials/Launching%20a%20Gazebo%20Simulation%20environment)
- [Adding a Source Workspace Tutorial](http://wiki.ros.org/Robots/Copernicus/Tutorials/Adding%20a%20Source%20Workspace)
- [Copernicus Simulation GitHub Repository](https://github.com/botsync/copernicus_simulation)
