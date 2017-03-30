## inmoov_description

### Summary

This package contains all the files needed for the URDF model of the InMoov. This includes .stl files (meshes/), .xacro and .gazebo files for the various parts of the robot (urdf/), and the generated .urdf file with its corrosponding master .xacro files (robots/). Also included are the files required to open Rviz and regenerate the URDF after changes are made to the .xacro files.

### Directions

Change directory to inmoov_description

To launch Rviz:

```
roslaunch inmoov_description rviz.launch
```

To regenerate the contents of the robot/ folder:

```
./urdf_regen.sh
```
**IMPORTANT**
If you need to edit anything in main .xacro files inside the robots folder, *only* edit the file inmoov.urdf.xacro; the other two will be overwritten when you run urdf_regen.sh 
