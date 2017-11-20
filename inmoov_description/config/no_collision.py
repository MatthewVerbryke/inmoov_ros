#!/usr/bin/env python
# Copyright 2017 University of Cincinnati
# All rights reserved. See LICENSE file at:
# https://github.com/MatthewVerbryke/inmoov-ros
# Additional copyright may be held by others, as reflected in the commit history.


import os
import sys

import lxml.etree as ET


def remove_collision_tags():
	"""
	Create a new model of the InMoov without collision tags.
	"""
	
	try:
		
		# Get the cwd
		setdir = os.getcwd()
		
		# Command line arguments
		package_path = sys.argv[1]
		robots_path = package_path + "/inmoov_description/robots"
		
		# Change directory to 'robots' file
		os.chdir(robots_path)
		
		# Import XML data from inmoov inmoov.xacro
		tree = ET.ElementTree()
		tree.parse("inmoov.urdf")
		root = tree.getroot()

		# Find all instances of the <collision> tag and delete them
		for collisions in root.xpath("//collision"):
			collisions.getparent().remove(collisions)
			
		# Write collision-less XML to new file
		tree.write("inmoov_no_collision.urdf")

	finally:
		
		# Change back to beginning cwd
		os.chdir(setdir)

# Run
remove_collision_tags()
