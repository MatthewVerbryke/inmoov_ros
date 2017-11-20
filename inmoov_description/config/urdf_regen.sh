#!/bin/bash
# Copyright 2017 University of Cincinnati
# All rights reserved. See LICENSE file at:
# https://github.com/MatthewVerbryke/inmoov-ros
# Additional copyright may be held by others, as reflected in the commit history.



#Source Setup
cd ~/catkin_ws/
source devel/setup.bash

#Get Paths
PACKAGE_PATH="/home/$USER/catkin_ws/src/inmoov_ros"

#Delete Old Files
cd $PACKAGE_PATH/inmoov_description/robots/
rm inmoov.xacro
rm inmoov.urdf
rm inmoov_no_collision.urdf

#Create New Files
rosrun xacro xacro.py -o inmoov.urdf inmoov.urdf.xacro
cp inmoov.urdf.xacro inmoov.xacro

#Create New "Collision-less" Model
cd $PACKAGE_PATH/inmoov_description/config/
python no_collision.py $PACKAGE_PATH
