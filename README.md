# AS4SR InMoov

## Summary

This repository contains a *work-in-progress* InMoov software stack, being used for research into robotic dual-arm manipulation at the University Of Cincinnati's Autonomous Systems for S.P.A.C.E. R.O.B.O.T.I.C.S.* (AS4SR) lab: <https://github.com/AS4SR/general_info/wiki>

Currently, it contains the following:
 - Gazebo compatable URDF model of the InMoov robot, adapted from <https://github.com/alansrobotlab/inmoov_ros>
   - Collision meshes based on .stl mesh files
   - Estimated inertial, damping, and friction properties
   - Transmission elements defined for all actuating joints
   - Sensors implimented in Gazebo
 - Controllers implimented for all actuated joints
 - A node to replicate a physical InMoov robots finger movement (similar to mimicking in Rviz)
 - Package for use with Gazebo

#### Sensors
 - Xbox Kinect 
 - Visual Cameras (one in each eye)
 - Contact Sensors (one in each fingertip)

## Packages

 - inmoov_control
 - inmoov_description 
 - inmoov_firmware **not currently used**
 - inmoov_gazebo
 - inmoov_meshes
 - inmoov_msgs **not currently used**
 - inmoov_tools **not currently used**

## Recommended OS/Programs

The software was developed and tested in:
 - Ubuntu 16.04 LTS
 - ROS Kinetic
 - Gazebo 7.0

## Current Issues

 - Inertial, damping, and friction values are estimates
 - Might not be able to simulate Passive Infrared (PIR) sensors in Gazebo

## Future Work

 - MoveIt! implimentation
 - Correction of inertial, damping, and friction values (based on experimntally determined values)
 - PID value adjustment?
 - VREP implimentation?
 - Add handpads for better grip?

## License

All currently-used packages (see above) use the BSD 3-clause license presented in the main license file. The one exception is the inmoov_meshes package, which uses the CC-NC-A license contained within that package.

###### *yes, this is an acronym

