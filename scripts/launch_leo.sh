#!/bin/bash

# Store current directory and change to the target directory
pushd ~/leo_ws/src/leo_simulator/leo_gazebo/launch/ > /dev/null

# If no arguments are provided, list all available worlds
if [ $# -eq 0 ]; then
    echo "Available worlds:"
    find worlds -name "*.launch" -exec basename {} .launch \;
else
    # Parse arguments
    while getopts "w:" opt; do
        case ${opt} in
            w)
                world=$OPTARG
                ;;
            \?)
                echo "Invalid option: -$OPTARG" 1>&2
                ;;
        esac
    done

    # Start Leo in the specified world
    if [ -n "$world" ]; then
        roslaunch leo_gazebo "${world}.launch"
    else
        echo "Please specify a world with the -w option."
    fi
fi

# Return to the original directory
popd > /dev/null