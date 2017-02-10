#!/usr/bin/bash

cd ~/catkin_ws/
source devel/setup.bash
cd ~/catkin_ws/src/inmoov_ros/inmoov_description/robots/
rosrun xacro xacro.py -o inmoov.urdf inmoov.urdf.xacro

cd ~/catkin_ws/
source devel/setup.bash
#cd ~/catkin_ws/src/inmoov_ros/
#roslaunch inmoov_gazebo inmoov_world.launch

