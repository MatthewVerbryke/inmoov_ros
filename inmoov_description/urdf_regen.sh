#!/bin/bash

#Source Setup
cd ~/catkin_ws/
source devel/setup.bash

#Delete Old Files
cd ~/catkin_ws/src/inmoov_ros/inmoov_description/robots/
rm inmoov.xacro
rm inmoov.urdf

#Create New Files
rosrun xacro xacro.py -o inmoov.urdf inmoov.urdf.xacro
cp inmoov.urdf.xacro inmoov.xacro





