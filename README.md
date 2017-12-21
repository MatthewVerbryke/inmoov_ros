# AS4SR InMoov

## Summary

This repository contains a *work-in-progress* InMoov software stack, being used for research into robotic dual-arm manipulation at the University Of Cincinnati's [Autonomous Systems for S.P.A.C.E. R.O.B.O.T.I.C.S.* (AS4SR) lab](https://github.com/AS4SR/general_info/wiki): 

Currently, it contains the following features:
 - A URDF model of the InMoov robot, adapted from Alan Timm's [Inmoov project](https://github.com/alansrobotlab/inmoov_ros):
   - Collision and collision-less models
   - Estimated inertial, damping, and friction properties
 - Gazebo-compatability:
   - Simulated sensors: visual cameras, kinect, contact sensors
 - MoveIt! integration

###### *yes, an acronym within an acronym

## Recommended OS/Programs

The software was developed and tested in:
 - Ubuntu 16.04 LTS
 - ROS Kinetic
 - Gazebo 7.9
 - MoveIt! for ROS Kinetic

## Installation

To install the current version of this repository to your machine, cd into your catkin workspace source directory and clone the repository:

```
git clone https://github.com/MatthewVerbryke/inmoov_ros
``` 

## Usage

### InMoov URDF 

Several tools exist to help view and edit the InMoov's URDF model. If you want to edit the model, only modify the files that end with ```.urdf.xacro```, found in the ```inmoov_description/robots``` and ```inmoov_description/urdf``` folders. Generally, you will not want to edit the ```.urdf``` files directly, as they are auto-generated and are also harder to sift through than the subcomponent files. Additionally, note that the contents of the ```inmoov_description/urdf/no_collision``` directory and the file ```inmoov_no_collisions.urdf.xacro``` are auto-generated as well, and any changes here will get overwritten.

After you are done editing, you can regenerate the complete urdf models, as well as collision-less xacro models, by switching into the ```inmoov_description/config``` directory, and running the autogeneration script:

```
./urdf_regen.sh
```

To launch a model of the InMoov in RViz from the top level directory, use:

```
roslaunch inmoov_description rviz.launch
```

### Gazebo

To launch an empty world with only the InMoov robot in it, use:

```
roslaunch inmoov_gazebo inmoov_world.launch
```

To launch the collision-less model of the InMoov, use:

```
roslaunch inmoov_gazebo inmoov_no_collision_world.launch
```

### MoveIt

**NOTE**: the MoveIt configuration for the InMoov is not fully completed, and changes may be made in the future.

To launch the InMoov model in Rviz with MoveIt (using fake joint controllers), use:

```
roslaunch inmoov_moveit demo.launch
```

To simulate the InMoov in Gazebo while using the MoveIt RViz GUI, first launch the InMoov in an empty Gazebo world:

```
roslaunch inmoov_gazebo inmoov_world.launch
```

Once Gazebo has launched cleanly, in a new terminal, launch the MoveIt execution file:

```
roslaunch inmoov_moveit moveit_planning_execution.launch
```

## Notes

 - Inertial, damping, and friction values are currently estimates; real values will be measured as a physical model is constructed.
 - The packages ```inmoov_firmware```, ```inmoov_msgs```, ```inmoov_tools``` are not currently used.

## Future Work

 - Correction of inertial, damping, and friction values (based on experimntally determined values)
 - Hardware implementation

## License

All currently-used packages (see above) use the BSD 3-clause license presented in the main license file. The one exception is the inmoov_meshes package, which uses the CC-NC-A license contained within that package.

The original branch is Copyright (c) Alan Timm (alansrobotlab).
All modifications are Copyright (c) University of Cincinnati.



