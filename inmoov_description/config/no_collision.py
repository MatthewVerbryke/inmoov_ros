#!/usr/bin/env python
# Copyright 2017 University of Cincinnati
# All rights reserved. See LICENSE file at:
# https://github.com/MatthewVerbryke/inmoov-ros
# Additional copyright may be held by others, as reflected in the commit history.


import fileinput
import os
import sys

import lxml.etree as ET


def remove_collision_tags(xacro_file, load_path, save_path):
    """
    Remove collision tags from the selected xacro file.
    """
                
    # Change directory to original xacro file location
    os.chdir(load_path)
    
    # Import XML data from inmoov inmoov.xacro
    tree = ET.ElementTree()
    tree.parse(xacro_file)
    root = tree.getroot()
    
    # Find all instances of the <collision> tag and delete them
    for collisions in root.xpath("//collision"):
        collisions.getparent().remove(collisions)
    
    # Determine file name
    if (xacro_file == "inmoov.urdf.xacro"):
        save_name = "inmoov_no_collision_temp.urdf.xacro"
    else:
        save_name = xacro_file
    
    # Go to save path
    os.chdir(save_path)
    
    # Write collision-less XML to new file
    tree.write(save_name, xml_declaration=True)
    
def replace_default_with_no_collisions():
    """
    Point 'inmoov_no_collision.urdf.xacro' to the correct location to get 
    the collision-less xacro parts.
    """
    
    try:
        
        # Open and Read inmoov_no_collisions
        temp_file = open("inmoov_no_collision_temp.urdf.xacro", "r")
        temp_hold_text = temp_file.read()
        temp_string = str(temp_hold_text)
        
        # Close file
        temp_file.close()
        
        # Replace 'default' with 'no_collisions'
        temp_string = temp_string.replace("default", "no_collisions")
        
        # Also, while we're in here, delete the contact sensors, which will cause problems without the collision definitions
        temp_string = temp_string.replace('<xacro:include filename="$(find inmoov_description)/urdf/contact_sensors.gazebo"/>', ' ')
        
        # Ensure results are a string
        xacro_content = str(temp_string)
            
        # Open config file
        target = open("inmoov_no_collision.urdf.xacro", "w")
            
        # Write to config file
        target.write(xacro_content)
        
    finally:
        
        # Close file
        target.close()
    
    
def main():
    """
    Find all default xacro files, remove collision tags, and save new 
    xacro files in the no_collisions directory.
    """
    
    try:
        
        # Get the cwd
        setdir = os.getcwd()
        
        # Command line argument
        package_path = sys.argv[1]
        
        # Paths to relevant directories
        robots_path = package_path + "/inmoov_description/robots"
        urdf_path = package_path + "/inmoov_description/urdf"
        default_path = urdf_path + "/default"
        no_collision_path = urdf_path + "/no_collisions"
        
        # Get filenames for all the files in the default directory
        xacros = os.listdir(default_path)
        
        # Move to default urdf directory
        os.chdir(default_path)
        
        # Remove the collision tags and save to 'no_collisions/'
        for xacro in xacros:
            remove_collision_tags(xacro, default_path, no_collision_path)
            
        # Additionally remove tags from the main xacro file
        remove_collision_tags('inmoov.urdf.xacro', robots_path, robots_path)
        
        # Move to default robots directory
        os.chdir(robots_path)
        
        # Replace 'default' with 'no_collisions' in the main xacro file
        replace_default_with_no_collisions()
        
    finally:
        
        # Change directory back to cwd
        os.chdir(setdir)    
    
        
# Run
main()    


#EOF
