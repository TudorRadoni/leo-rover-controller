# RCS Project - Documentation

## ROS Installation

I used Ubuntu 20.04 LTS for this project. I followed the instructions on the ![ROS website](http://wiki.ros.org/noetic/Installation/Ubuntu) to install ROS Noetic. I used the "Desktop-Full Install" option.

## Choosing a robot

To choose a robot, I looked at the ![ROS Robots list with tag #noetic](https://robots.ros.org/tags/#noetic).

<!-- TODO: Trebuie sa zic ce robot am ales -->

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

<!-- TODO: Aici e pentru husky! -->

```bash
source devel/setup.bash
export HUSKY_GAZEBO_DESCRIPTION=$(rospack find husky_gazebo)/urdf/description.gazebo.xacro
cd src/husky/husky_gazebo/launch/
roslaunch husky_gazebo empty_world.launch
```

PENTRU DATA VIITOARE:

- [TIAGo Robot Simulation Files](http://wiki.ros.org/Robots/TIAGo#Simulation_files)
- [Copernicus Robot Information](http://wiki.ros.org/Robots/Copernicus)
- [Launching a Gazebo Simulation Environment Tutorial](http://wiki.ros.org/Robots/Copernicus/Tutorials/Launching%20a%20Gazebo%20Simulation%20environment)
- [Adding a Source Workspace Tutorial](http://wiki.ros.org/Robots/Copernicus/Tutorials/Adding%20a%20Source%20Workspace)
- [Copernicus Simulation GitHub Repository](https://github.com/botsync/copernicus_simulation)
- [ROS Answer on xacro problem](https://answers.ros.org/question/122021/xacro-problem-invalid-param-tag-cannot-load-command-parameter-robot_description/)
