# AS4SR InMoov

## Summary

This repository contains a *work-in-progress* InMoov software stack, being used for research into robotic dual-arm manipulation at the University Of Cincinnati's Autonomous Systems for S.P.A.C.E. R.O.B.O.T.I.C.S.* (AS4SR) lab: <https://github.com/AS4SR/general_info/wiki>

Currently, it contains the following:
 - Gazebo compatable URDF model of the InMoov robot, adapted from <https://github.com/alansrobotlab/inmoov_ros>
   - Collision meshes based on .stl files
   - Estimated inertial properties (moments of inertia and masses)
   - Estimated damping and friction properties
   - Transmission elements defined for all actuating joints
 - Controllers implimented for all actuated joints
 - Package for use with Gazebo

## Packages

 - inmoov_control
 - inmoov_description 
 - inmoov_firmware **not currently used**
 - inmoov_gazebo
 - inmoov_msgs **not currently used**
 - inmoov_tools **not currently used**
 - robot_editor **not currently used**

## Recommended OS/Programs

The software was developed and tested in:
 - Ubuntu 16.04 LTS
 - ROS Kinetic
 - Gazebo 7.0

## Current Issues

 - Inertial, damping, and friction values are estimates
 - Joint mimicking is not supported in Gazebo
 - ~~Right ring and pinky not functioning correctly~~

## Future Work

 - ~~Fix right ring/pinky issue~~
 - Joint mimicking implimentation
 - Add sensors
 - MoveIt! implimentation
 - Correction of inertial, damping, and friction values (based on experimntally determined values)
 - VREP implimentation?
 - Add handpads for better grip?


###### *yes, this is an acronym

