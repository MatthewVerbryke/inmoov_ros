#!/bin/bash
# Copyright 2017 University of Cincinnati
# All rights reserved. See LICENSE file at:
# https://github.com/MatthewVerbryke/inmoov-ros
# Additional copyright may be held by others, as reflected in the commit history.


#Source Setup
cd ~/catkin_ws/
source devel/setup.bash

#Get Path
PACKAGE_PATH="/home/$USER/catkin_ws/src/inmoov_ros"

#Delete Old Files
cd $PACKAGE_PATH/inmoov_description/robots
rm inmoov.urdf
rm inmoov_no_collision.urdf
rm inmoov_no_collision.urdf.xacro

cd $PACKAGE_PATH/inmoov_description/urdf/no_collisions/
rm asmArm.urdf.xacro
rm asmBase.urdf.xacro
rm asmFace.urdf.xacro
rm asmHead.urdf.xacro
rm asmTorso.urdf.xacro
rm leftHand.urdf.xacro
rm rightHand.urdf.xacro

#Create New "Collision-less" Model
cd $PACKAGE_PATH/inmoov_description/config/
python no_collision.py $PACKAGE_PATH

#Remove the temporary file generated
cd $PACKAGE_PATH/inmoov_description/robots/
rm inmoov_no_collision_temp.urdf.xacro

#Create URDF Files (largely for kicks?)
rosrun xacro xacro.py -o inmoov.urdf inmoov.urdf.xacro
rosrun xacro xacro.py -o inmoov_no_collision.urdf inmoov_no_collision.urdf.xacro
